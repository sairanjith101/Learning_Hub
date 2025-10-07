# How to create relationships between models (OneToOneField, ForeignKey, ManyToManyField)?

# In Django, we can create relationships using special fields:

# * `OneToOneField` – for one-to-one relationship.
# * `ForeignKey` – for one-to-many relationship.
# * `ManyToManyField` – for many-to-many relationship.

# Simple Explanation:

# `OneToOneField`: One record in one model is linked to one record in another model.
#   Example: One user has one profile.


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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    # ManyToMany relationship between Student and Course
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name


# `on_delete=models.CASCADE` means if the related object is deleted, this object will also be deleted.
# Django handles these relationships and creates proper join tables in the database.

