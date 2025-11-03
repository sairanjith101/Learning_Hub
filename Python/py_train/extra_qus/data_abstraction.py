class rectangle:

    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    
rect = rectangle(5,3)
print(f'Area: {rect.area()}')
print(f'Area: {rect.perimeter()}')