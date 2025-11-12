# Q: Define a model Employee with optional phone number and active status default as True.

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)
