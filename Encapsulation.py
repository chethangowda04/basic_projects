class Employee:
    def __init__(self, name, project):
        self._name = name
        self._project = project
emp = Employee("team bepractical",1)
print("name:", emp._name)
print("project", emp._project)



###protected###
num = 9110462859
s_id = ["bepractical"]
pas = 815689
id_c = input("enter your id::")
pa = int(input("enter the password::"))
class student:
    def check_give(self):
        self._num = num
        self._s_id = s_id
        self.pas = pas
        self.pa = pa
        self.id_c = id_c
        if id_c in s_id and pa == pas:
            print(num)
        else:
            print("wrong id or password")
s = student()
s.check_give()



##private###
class employee:
    def __init__(self, name, project):
        self.name = name
        self.__project = project
emp = employee('team bepractical', 1)
print("name:", emp.name)
print("project:", emp._employee__project)


###public, protected, private with inheritance###
class Teacher:
    val1 = None
    _val2 = None
    __val3 = None

    def __init__(self,val1, val2, val3):
        self.val1 = val1
        self._val2 = val2
        self.__val3 = val3

    def disppublicmembers(self):
        print("the public members are:", self.val1)

    def _dispprotectedmembers(self):
        print("the protected members are:", self._val2)

    def __dispprivatemembers(self):
        print("the private members are:", self.__val3)

    def accessprivatemembers(self):
        self.__dispprivatemembers()

class child(Teacher):
    def __init__(self, val1, val2, val3):
        Teacher.__init__(self, val1, val2, val3)

    def accessprotectedmembers(self):
        self._dispprotectedmembers()

obj1 = child("hello", "simon", 81050)
obj1.disppublicmembers()
obj1.accessprotectedmembers()
obj1.accessprivatemembers()



