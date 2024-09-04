###Abstraction###

##to find area of shapes
class shapes:
    def area(self):
        pass
class rectangle:
    length = 6
    breadth = 4
    def area(self):
        return self.length*self.breadth
class circle:
    radius = 7
    def area(self):
        return 3.14*self.radius*self.radius
class square:
    length = 4
    def area(self):
        return self.length*self.length

r = rectangle()
c = circle()
s = square()

print("area of rectangle is::", r.area())
print("area of circle is::", c.area())
print("area of square is::", s.area())


##arithmatic operators
class calculator:
    def calc(self):
        pass

class addition:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a+self.b
class subtraction:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a-self.b
class multiplication:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a*self.b
class division:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a/self.b
class floor_devision:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a//self.b
class modulus:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a%self.b
class exponantial:
    a = int(input("enter a value::"))
    b = int(input("enter b value::"))
    def calc(self):
        return self.a**self.b

a = addition()
s = subtraction()
m = multiplication()
d = division()
f = floor_devision()
mod = modulus()
e = exponantial()

print("the addition of a given numbers is::", a.calc())
print("the subtraction of a given numbers is::", s.calc())
print("the multiplication of a given numbers is::", m.calc())
print("the division of a given numbers is::", d.calc())
print("the floor division of a given numbers is::", f.calc())
print("the modulus of a given numbers is::", mod.calc())
print("the exponantial of a given numbers is::", e.calc())
