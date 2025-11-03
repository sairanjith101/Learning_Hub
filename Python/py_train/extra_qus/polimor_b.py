class shape:

    def intro(self):
        print("A shape is the outline or external boundary of an object")

    def area(self):
        print("Area is the amount of space occupied by a two-dimensional figure")

class circle(shape):

    def area(self):
        print("Circle area find formula : A=πr2")

class square(shape):

    def area(self):
        print("Square area find formula: a(x + m)2 + n = a(x + m)2 + n")

obj_shape = shape()
obj_circle = circle()
obj_square = square()

obj_shape.intro()
obj_shape.area()

obj_circle.intro()
obj_circle.area()

obj_square.intro()
obj_square.area()