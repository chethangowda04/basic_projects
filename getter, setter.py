class person:
    def __init__(self,name,age=0):
        self.name=name
        self.__age=age
    def display(self):
        print(self.name)
        print(self.__age)

    def getage(self):
        print(self.__age)

    def setage(self,age):
        self.__age=age

print(" the age of the person is:: ")
person=person('dev',30)
person.display()
print(" after revising the age of the person::")
person.setage(35)
person.getage()

class stud_abc:
    def __init__(self, totalmarks=0, totalsub=0):
        self.__totalmarks = totalmarks
        self.__totalsub = totalsub

    def get_totalmarks(self):
        return self._totalmarks

    def set_totalmarks(self,x):
        self._totalmarks = x

    def get_totalsub(self):
        return self._totalsub

    def set_totalsub(self, y):
        self._totalsub = y

student = stud_abc()
student.set_totalmarks(349)
student.set_totalsub(5)


print("total marks:" + str(student.get_totalmarks()))
print("total subject:" + str(student.get_totalsub()))
print("average:" + str(student._totalmarks / student._totalsub))


class student:
    def __init__(self, name=0, marks=0):
        self.name = name
        self.__marks = marks


    def get_name(self):
        return self.name

    def set_name(self, a):
        self.name = a

    def get_marks(self):
        return self.marks

    def set_marks(self, b):
        self.marks = b

stud = student()
stud.set_name("Vinayak")
stud.set_marks(10)


print("name:",  str(stud.get_name()))
print("marks:",  str(stud.get_marks()))


class student:
    def __init__(self,name,marks=0):
        self.name=name
        self.__marks=marks
    def display(self):
        print(self.name)
        print(self.__marks)

    def getmarks(self):
        print(self.__marks)

    def setmarks(self,marks):
        self.__marks=marks

print(" the name and marks of the student is:: ")
stud=student('Vinayak',10)
stud.display()



class student:
    def __init__(self, name:str):
        self.name:str=name
        self.__marks:int=0


    def get_marks(self):
        return self.name+" got"+str(self.__marks)

    def set_marks(self,marks:int):
        self.__marks= marks

    def _str_(self):
        return "student name is "+ self.name


stud = student("vinayak")
print(stud)
stud.set_marks(10)
marks_stud_got=stud.get_marks()
print(marks_stud_got)




property function using getter and setter
class person:
    def __init__(self,name):
        self._name=name

    def get_name(self):
        print('getting name...')
        return self._name
    def set_name(self,value):
        print('setting name to:',value)
        self._name=value

    def del_name(self):
        print('deleting names...')
        del self._name
    name=property(get_name,set_name,del_name)

p=person('david')
print(p.name)
p.name='rocky'
del p.name


###Property decorator  using getter and setter
class person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("setting name to:", value)
        self._name = value

    @name.deleter
    def name(self):
        print("deleting name...")
        del self._name

p = person("David")
print(p.name)
p.name = "Rocky"
del p.name