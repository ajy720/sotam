from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Users(AbstractUser):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=30)

    std_id = models.CharField(max_length=8, blank=True)
    major = models.CharField(max_length=30, blank=True)
    college = models.CharField(max_length=20, blank=True)

    is_admin = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_created=True, auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username}({self.email})'
