# Q: Fetch all active employees ordered by name.

from models import Employee

Employee.objects.filter(is_active=True).order_by('name')

# Q: Get all students in the “CSE” department.

from models import Student

Student.objects.filter(department__name='CSE')



