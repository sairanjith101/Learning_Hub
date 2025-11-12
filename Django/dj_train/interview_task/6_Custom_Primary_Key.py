# Q: Create a model with a custom primary key field called emp_id.

from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
