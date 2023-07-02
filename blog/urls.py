from django.urls import path
from . import views
import blog.views


urlpatterns = [
    path("", blog.views.index),
]