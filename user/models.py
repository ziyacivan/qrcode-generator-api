from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from user.managers import UserManager

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'