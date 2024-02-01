from abc import ABC, abstractmethod

# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Parrot(Animal):
    def speak(self):
        return "Squawk!"

# Abstract Creator
class AnimalCreator(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class DogCreator(AnimalCreator):
    def create_animal(self):
        return Dog()

class CatCreator(AnimalCreator):
    def create_animal(self):
        return Cat()

class ParrotCreator(AnimalCreator):
    def create_animal(self):
        return Parrot()

# Client Code
parrot_creator = ParrotCreator()
parrot = parrot_creator.create_animal()
print(parrot.speak())  # Squawk!
