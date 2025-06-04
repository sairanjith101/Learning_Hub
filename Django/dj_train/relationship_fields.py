#🔵 1. OneToOneField
#🗣️ OneToOneField is used to create a one-to-one relationship between two models, like each user having one profile.

from django import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    bio = models.TextField()


#🔵 2. ForeignKey (Many-to-One)
# Many-to-one relationship means, many records in one model are linked to a single record in another model.
# In Django, we use ForeignKey field for this."

class Course(models.Model):
    title = models.CharField(max_length = 100)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, on_delete = models.CASECADE)

# 🔵 3. ManyToManyField
# 🗣️ "ManyToManyField links multiple rows of one model to multiple rows of another model."

class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField("Student", through="Enrollment")

class Student(models.Model):
    name = models.CharField(max_length=100)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True)

# views Query

from .models import Student

joined_student = Student.objects.filter(enrollment__isnull=False).distinct()

not_joined_student = Student.objects.filter(enrollment__isnull=True)

