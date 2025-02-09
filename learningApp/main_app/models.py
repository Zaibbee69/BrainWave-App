from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Will be using Django's built in User model for app
class User(AbstractUser):
    pass