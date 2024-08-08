##Multilevel Inheritance
class Shape:
    def __init__(self):
        pass  # Initialize any common attributes here if needed


class RectangleBase(Shape):
    def __init__(self, width, height):
        super().__init__()  # Call the initializer of the base class
        self.width = width
        self.height = height


class Rectangle(RectangleBase):
    def __init__(self, width, height):
        super().__init__(width, height)  # Call the initializer of the intermediate class

    def area(self):
        return self.width * self.height  # Calculate and return the area


rect = Rectangle(5, 10)
print("The area of the rectangle is:", rect.area())