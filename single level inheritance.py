class ABC_comp:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def comp_info(self):
        print("we are product based company")
class employee(ABC_comp):
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address
    def emp_dtls(self):
        print(self.name, self.age, self.salary, self.address)
E1 = employee(name = "chethan", age = 23, salary = 25000, address = "bengaluru")
E1.comp_info()
E1.emp_dtls()


class Be_practical:
    def __init__(self, name, age, course, institute):
        self.name = name
        self.age = age
        self.course = course
        self.specification = institute
    def institute_info(self):
        print("Be Practical is a technical training institute")
class student(Be_practical):
    def __init__(self, name, age, course, institute, address):
        self.name = name
        self.age = age
        self.course = course
        self.institute = institute
        self.address = address
    def stud_dtls(self):
        # print(self.name,"is", self.age,"year old, he is studying", self.course,"in", self.institute,"at", self.address)
        print(f"""name::{self.name}
age::{self.age}
course opted::{self.course}
specialised in::{self.institute}
location::{self.address}""")

s1 = student("chethan", 23, "python", "ISE", "Basaveshwarnagar")
s1.institute_info()
s1.stud_dtls()