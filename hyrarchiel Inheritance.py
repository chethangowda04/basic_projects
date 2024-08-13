import math
class maths:
    def math_info(self):
        print("""
maths has a three types, i.e arithmatic, algebra and geometry.
let's see an example for each.""")

class algebra(maths):
    def alge_info(self):
        print("\nexample for algebra")
    def heart_pattern(self):
        for row in range(6):
            for col in range(7):
                if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


    def amstrong_num(self):
        print("\nTo find amstrong number")
        num = int(input("enter any 3 digit number::"))
        print("\n",num)
        sum = 0
        temp = num
        while temp > 0:
            d = temp % 10
            sum += d * d * d
            temp //= 10
        if sum == num:
            print("It is armstrong number")
        else:
            print("It is not armstrong number")


class geometry(maths):
    def geo_info(self):
        print("\n example for geometry")

    def area_of_circle(self):
        print("area of circle")
        r = int(input("enter radius of circle::"))
        pi = 3.14
        print("area of circle is:",pi * r ** 2)
    def area_of_rectangle(self):
        print("\n area of rectangle")
        l = int(input("enter length of rectangle::"))
        b = int(input("enter bredth of rectangle::"))
        h = int(input("enter height of rectangle::"))
        print("areaa of rectangle is:",l * b * h)

class arithmatic(maths):
    def arth_info(self):
        print("\n example for arithmatic")
    def factorial_of_list(self):
        lst = range(1, 6)
        for number in lst:
            factorial = math.factorial(number)
            print(f"Factorial of {number} is {factorial}")


a=maths()
a.math_info()

b = algebra()
b.alge_info()
b.heart_pattern()
b.amstrong_num()

c=geometry()
c.geo_info()
c.area_of_circle()
c.area_of_rectangle()


d = arithmatic()
d.arth_info()
d.factorial_of_list()