from rest_framework import serializers
from blog.models import Post, Tag, Comment
from blango_auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        read_only_fields = ["modified_at", "created_at"]

class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")

class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="value", many=True, queryset=Tag.objects.all()
    )
    author = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name="api_user_detail", lookup_field="email"
    )
    author_email = serializers.EmailField(source='author.email', read_only=True)

    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ],
        read_only=True,
    )

    exclude = ["ppoi"]

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'summary', 'content', 'author', 'author_email', 'published_at', 'modified_at', 'created_at', 'tags']
        read_only_fields = ["modified_at", "created_at"]

class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)

    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("square_crop", "crop__200x200"),
        ],
        read_only=True,
    )

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ['comments']

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments", [])
        tags_data = validated_data.pop("tags", [])

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(value=tag_data)
            instance.tags.add(tag)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()

        return instance

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['url', 'id', 'value']