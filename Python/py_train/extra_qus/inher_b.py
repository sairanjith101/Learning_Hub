class vehicle:

    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def display(self):
        print(self.brand)
        print(self.year)

class truck(vehicle):

    def __init__(self, brand, year, tank, load):
        self.tank = tank
        self.load = load

        vehicle.__init__(self,brand,year)

    def details(self):
        print(f'Brand: {self.brand}')
        print(f'year: {self.year}')
        print(f'Tank: {self.tank}')
        print(f'Load: {self.load}')

autobikes = truck("Mahendra", 2021, "30 L", "30 Tones")
autobikes.display()
autobikes.details()