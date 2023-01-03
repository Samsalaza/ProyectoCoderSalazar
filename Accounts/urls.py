from django.urls import path
from Accounts.views import *

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('login/', login_request, name="login"),
    path('profile/', profile),
    path("", start),
]
