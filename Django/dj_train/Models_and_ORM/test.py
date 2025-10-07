from myapp.models import Student

# create - insert data from db

# option 1
student = Student.objects(name="sai", age=10)
student.save()

# Option 2
Student.objects.create(name="sai", age=10)

# Read - fetch data from db

# a) get all
student = Student.objects.all()
# b) get
student = Student.objects.get(id=1)
# c) filter
student = Student.objects.filter(age__gte=10)
# d) order by
student = Student.objects.order_by("name")

# Update - modify existing records

# option 1
student = Student.objects.get(id=1)
student.name("Raj")
student.save()

# Option 2
Student.objects.filter(id=1).update(name="Raj")

# delete - delete record from db
# option 1
student = Student.objects.get(id=1)
student.delete()

# option 2
Student.objects.filter(age_lt=10).delete()

# exact - case sensitive

Student.Objects.filter(age_exact=18)
Student.objects.filter(name_exact="Ravi")

# iexact - case insenstive

Student.objects.filter(name__iexact="Ravi")

# gt - grater than

Student.objects.filter(age__gt=10)

# gte - greater than equal to

Student.objects.filter(age__gte=20)

# lt - less than
Student.objects.filter(age__lt = 10)

# lte - less than equal to
Student.objects.filter(age__lte=10)

# contains - case sensitive
Student.filter(name__contains="vi")

# icontains - case insensitive
Student.filter(name__icontains="VI")

# in - in a list

Student.objects.filter(age__in=[18,20])
