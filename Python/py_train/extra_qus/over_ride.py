class employee:

    def get_salary(self):
        print("10K per month salary")

class manager(employee):

    def get_salary(self):
        print("25k per month salary")

emp = employee()
man = manager()

emp.get_salary()
man.get_salary()