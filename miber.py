class animal(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
class Dog(animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def make_sound(self):
        return "Woof!"

class Cat(animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def make_sound(self):
        return "Meow!"

pet1 = Dog("Buddy")
pet2 = Cat("Whiskers")

print(f"{pet1.name} is a {pet1.species} and says {pet1.make_sound()}")
print(f"{pet2.name} is a {pet2.species} and says {pet2.make_sound()}")
    