from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField('email address', blank=True, unique=True, db_index=True)
    avatar = models.ImageField(verbose_name='Avatar', blank=True, null=True, upload_to='avatars/')
