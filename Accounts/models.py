from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Users(models.Model):
    user_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)

    def __str__(self):
           return self.user_name

class userAvatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"