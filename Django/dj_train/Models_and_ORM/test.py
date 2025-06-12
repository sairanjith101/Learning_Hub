from .models import Student

# get all
student = Student.objects.all()

# get one
student = Student.objects.get(id=1)

# filter
student = Student.objects.filter(age__gte=18)

# orderby
student = Student.objects.order_by('name')

# update
student = student.objects.get(id=1)
student.name = "Raj"
student.save()

student = Student.objects.filter(id=1).update(name="Raj")

# delete
student = student.objects.get(id=1)
student.delete()

student = Student.objects.filter(id=1).delete()