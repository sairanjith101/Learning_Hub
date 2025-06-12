# Model: A Django model is a Python class that defines the structure of a database table 
# and handles the interaction between the application and the database.

from django.db import models

class Book(models.Models):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title