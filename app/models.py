from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Register(AbstractUser):
    email_or_phone = models.CharField(max_length=200, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=200)

    USERNAME_FIELD = 'email_or_phone'
    REQUIRED_FIELDS = []








