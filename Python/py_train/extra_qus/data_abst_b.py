from abc import ABC, abstractmethod

class animal:

    @abstractmethod
    def make_sound(self):
        pass

class dog(animal):

    def make_sound(self):
        return "Wow"
    
class cat(animal):

    def make_sound(self):
        return "Meow"
    
animal = animal()
dog = dog()
cat = cat()

print(f"Dog make sound: {dog.make_sound()}")
print(f"Cat make sound: {cat.make_sound()}")