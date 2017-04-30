from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(verbose_name='Avatar', blank=True, null=True, upload_to='avatars/')
