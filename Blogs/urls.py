from django.urls import path
from Blogs.views import *

urlpatterns = [
    path('', index),
    path('review/', blogForm, name="blogForm"),
    path('newPlace/', newPlaceForm, name="newPlaceForm"),
    path('searchPlace/', newPlaceSearch, name="newPlaceSearch"),
    path('search/', searchPlace, name="searchPlace"),
    path('placesList/', placesList, name="placesList"),
    path('placesDetail/<id>', placeDetails , name="placeDetails"),
]
