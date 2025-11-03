class father:

    def __init__(self,name,ID):
        self.name = name
        self.id = ID

    def display(self):
        print(self.name)
        print(self.id)

    def details(self):
        print(f'My father name: {self.name}')
        print(f'My Father ID: {self.id}')

class son(father):

    def __init__(self, name, ID, dept, salary):

        self.dept = dept
        self.salary = salary

        father.__init__(self,name,ID)

    def details(self):
        print(f'My name: {self.name}')
        print(f'ID : {self.id}')
        print(f'Department: {self.dept}')
        print(f'Salaray: {self.salary}')

child = son('Sai', 1234, "Mech", 10000)

child.display()
child.details()
