class bird:

    def intro(self):
        print("There are many types of birds")

    def fly(self):
        print("So many birds are fly but some cannot")

class sparrow(bird):

    def fly(self):
        print("Sparrow can Fly")

class Chicken(bird):

    def fly(self):
        print("Chicken cannot fly")

class peackack(bird):

    def fly(self):
        print("Peackack can fly")

obj_brid = bird()
obj_spr = sparrow()
obj_chi = Chicken()
obj_peak = peackack()

obj_brid.intro()
obj_brid.fly()

obj_spr.intro()
obj_spr.fly()

obj_chi.intro()
obj_chi.fly()