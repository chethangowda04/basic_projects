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




###school Bag###
class school_bag:
    def __init__(self, tng1, tng2, tng3, tng4):
        self.tng1 = tng1
        self.tng2 = tng2
        self._tng3 = tng3
        self.__tng4 = tng4

    def public_things(self):
        print(f"The {self.tng1} are the most important thing in the school bag.")

    def public_thing(self):
        print(f"Along with {self.tng1}, {self.tng2} is maandatory in school.")

    def _protected_thing(self):
        print(f"In school bags {self._tng3} are bit protected as the chances of loosing {self._tng3} are very high.")

    def access_protected(self):
        self._protected_thing()

    def __private_thing(self):
        print(f"In school days the {self.__tng4} are kept private by students, as they don't wish to share their marks.")

    def access_private(self):
        self.__private_thing()


    # def __init__(self, tng1, tng2, tng3, tng4):
    #     school_bag.__init__
obj = school_bag("book", "dairy", "pens", "markssheet")
obj.public_things()
obj.public_thing()
obj.access_protected()
obj.access_private()

