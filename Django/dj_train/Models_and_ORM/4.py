# How to create relationships between models (OneToOneField, ForeignKey, ManyToManyField)?

# In Django, we can create relationships using special fields:

# * `OneToOneField` – for one-to-one relationship.
# * `ForeignKey` – for one-to-many relationship.
# * `ManyToManyField` – for many-to-many relationship.

# Simple Explanation:

# `OneToOneField`: One record in one model is linked to one record in another model.
#   Example: One user has one profile.

from django import models

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()


# `ForeignKey`: One record in one model can be linked to many records in another.
#   Example: Many books belong to one author.

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

# `ManyToManyField`: Many records in one model linked to many records in another.
#   Example: A student can take many courses, and a course can have many students.

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, through='Enrollment')

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)

# `on_delete=models.CASCADE` means if the related object is deleted, this object will also be deleted.
# Django handles these relationships and creates proper join tables in the database.

