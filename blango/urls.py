"""samples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.blog, name='blog')
Class-based views
    1. Add an import:  from other_app.views import Blog
    2. Add a URL to urlpatterns:  path('', Blog.as_view(), name='blog')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    # re_path(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep
]
