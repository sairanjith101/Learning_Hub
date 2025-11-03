from collections import namedtuple

rectangle = namedtuple("rectangle", ["width", "height"])
rec = rectangle(50,30)

def area(rectangle):
    return rectangle.width * rectangle.height

def perimeter(rectangle):
    return 2 * (rectangle.width + rectangle.height)

print("Area: ", area(rec))
print("Perimeter: ", perimeter(rec))