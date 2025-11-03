class car:

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

obj = car("BMW", "Mini Cooper", 2007)
print(obj.brand)
print(obj.model)
print(obj.year)