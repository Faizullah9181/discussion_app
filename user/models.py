from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Users(AbstractUser):
    username = models.CharField(max_length=100, unique=True,null=False, blank=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    mobile_no = models.CharField(max_length=15, blank=True)
    image = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=500, blank=True)
    dob = models.DateField(null=True, blank=False)
    last_modified = models.DateTimeField(auto_now_add=True)
    is_profile_complete = models.BooleanField(default=False)

    
    REQUIRED_FIELDS = ['email']






