#class using init function
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
S1 = Student("Chethan", 23)
print(S1.name, S1.age)

class cars:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color
S1 = cars("Baleno", 2018, "pearl white")
print(S1.name, S1.model, S1.color)