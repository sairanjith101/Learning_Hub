from myapp.models import Student
from django.db.models import Avg, Sum

Student.objects.aggregate(Avg("age"))

Student.objects.aggregate(Sum('age'))

from django.db.models import Count

Student.objects.annotate(book_count=Count("Book"))


for std in Student:
    print(Student.name, Student.age)