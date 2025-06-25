from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # sets value only once, on creation
    updated_at = models.DateTimeField(auto_now=True)      # updates value every time the object is saved

    def __str__(self):
        return self.title
