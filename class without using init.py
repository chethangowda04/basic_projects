##class without using init function
class Student:
    def stu_info(self):
        self.name = input("enter name::")
        self.age = int(input("enter age::"))
    def display(self):
        print(self.name, self.age)
S1 = Student()
S1.stu_info()
S1.display()


class cars:
    def car_info(self):
        self.name = input("enter car name::")
        self.model = input("enter car model::")
        self.color = input("enter car color::")
    def display(self):
        print(self.name, self.model, self.color)
c1 = cars()
c1.car_info()
c1.display()