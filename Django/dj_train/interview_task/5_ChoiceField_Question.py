# Q: Create a Task model where the status field can only have three values — Pending, In Progress, or Done.

from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('D', 'Done'),
    ]
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
