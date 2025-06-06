from django.db import models

# Create your models here.

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} by {self.instructor} on {self.date_time}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} booked {self.fitness_class.name}"
    
