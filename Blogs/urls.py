from django.urls import path
from Blogs.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index),
    path('review/', blogForm, name="blogForm"),
    path('newPlace/', newPlaceForm, name="newPlaceForm"),
    path('searchPlace/', newPlaceSearch, name="newPlaceSearch"),
    path('search/', searchPlace, name="searchPlace"),
    path('placesList/', placesList, name="placesList"),
    path('placesDetail/<id>', placeDetails , name="placeDetails"),
    path('allBlogs/', allBlogs , name="allBlogs"),
    path('blog/<id>', blogPost , name="blogPost"),
    path('editBlog/<id>', editBlog , name="editBlog"),
    path('userPost', userPosts, name="userPosts"),
    path('deletePost/<id>', deletePost, name="deletePost"),
]
