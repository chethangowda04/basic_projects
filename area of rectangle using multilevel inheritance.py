class mathematics:
    import math

    def math_info(self):
        print("\nmathematics is the study of numbers and how they are related to each other and to the real world!!")

class algebra(mathematics):

    def alge_info(self):
        print("""\nAlgebra is a branch of mathematics that uses mathematical statements to describe relationships between things that vary.""")

class area_of_rectangle(algebra):
    # def __init__(self, length, breadth,height):
    #     self.length = length
    #     self.breadth = breadth
    #     self.height = height
    def values(self):
        length = int(input("\nenter length of the rectangle::"))
        breadth = int(input("enter breadth of the rectangle::"))
        height = int(input("enter height of the rectangle::"))
        print(length*breadth*height)

        return "Thank you"


val = area_of_rectangle()

val.math_info()
val.alge_info()
print(val.values())
