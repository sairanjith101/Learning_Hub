from myapp.models import Student

# create

student = Student(name = 'Ravi', age = 20)
student.save()

student = Student.objects.create(name='Ravi', age=20)

# read

student = Student.objects.all()

student = Student.objects.get(id=id)

student = Student.objects.filter(age__gte=8)

student = Student.objects.order_by('name')

# update

student = Student.objects.get(id=id)
student.name = "Raj"
student.save()

student = Student.objects.filter(id=id).update(name="Raj")


# delete

student = Student.objects.get(id=id)
student.delete()

student = Student.objects.filter(id=id).delete()