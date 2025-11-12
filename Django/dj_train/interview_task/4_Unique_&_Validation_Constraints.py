# Q: Create a model User with unique email and username fields.

# 🟢 Case 1: You need to CREATE your own model

from django.db import models
from django.conf import User

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
# 🔵 2. Use Django’s default User model

from django.contrib.auth.models import User

# Case 3: You want to USE Django’s built-in User model

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

# In settings.py:
AUTH_USER_MODEL = 'yourapp.CustomUser'

