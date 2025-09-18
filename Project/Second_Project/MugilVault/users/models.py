from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    storage_quota = models.BigIntegerField(default=5*1024*1024*1024)  # 5 GB

    def __str__(self):
        return self.username