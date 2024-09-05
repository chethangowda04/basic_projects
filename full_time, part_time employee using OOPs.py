class employee:
    def __init__(self,name):
        self.name = name
    def salary(self):
        pass


class full_time_employee(employee):
    def salary(self):
        days = int(input("Please enter how many days the employee has logged in::"))
        fsalary =  days*1200
        print(f"the salary of {self.name} this month is {fsalary} ")


class part_time_employee(employee):
    def salary(self):
        hours = int(input("Please enter how many hours the employee has worked this month::"))
        psalary = hours*150
        print(f"the salary of {self.name} this month is {psalary} ")


name = input("enter employee name::")

emp_type = int(input("""Please select the employee type
1 Full time employee
2 part time employee
"""))

if emp_type == 1:
    emp = full_time_employee(name)

elif emp_type == 2:
    emp = part_time_employee(name)
else:
    print("enter valid employee type")
    exit()

emp.salary()

