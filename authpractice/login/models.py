from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username=None
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255,unique=True)
    password=models.CharField(max_length=128)
    
    USERNAME_FIELD='email'    
    REQUIRED_FIELDS=['name']

    objects=UserManager()

    def __str__(self):
        return f'{self.name}-{self.email}'