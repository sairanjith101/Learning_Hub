# Q: Define a model for uploading profile pictures.

from django.db import models

class Profile(models.Model):
    user = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profiles/')
