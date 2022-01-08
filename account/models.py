# from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#test

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(max_length=200)
    bio = models.TextField()
    # joine = models.DateTimefield(auto_now=True)

    def __str__(self):
        return str(self.user.username)
