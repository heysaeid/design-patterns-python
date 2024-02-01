import copy
from typing import Self


class Prototype:
    def clone(self) -> Self:
        return copy.copy(self)


class Car(Prototype):
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car Model: {self.model}"


original_car = Car("Sedan")
copied_car = original_car.clone()
copied_car.model = "SUV"
print(original_car)
print(copied_car)