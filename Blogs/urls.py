from django.urls import path
from Blogs.views import *
from Blogs.forms import BlogForm

urlpatterns = [
    path('', index),
    path('review/', blogForm, name="blogForm"),
]
