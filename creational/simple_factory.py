# Product
class Animal:
    def speak(self):
        ...


# Concrete Product
class Dog(Animal):
    def speak(self):
        return "Woof!"


# Concrete Product
class Cat(Animal):
    def speak(self):
        return "Meow!"


# Concrete Factory
class AnimalFactory:
    def create_animal(self, animal_type: str):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")


animal_factory = AnimalFactory()
animal = animal_factory.create_animal("dog")
animal.speak()
animal = animal_factory.create_animal("cat")
animal.speak()
