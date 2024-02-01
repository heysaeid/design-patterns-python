# Builder Interface
class PizzaBuilder:
    def build_dough(self):
        ...

    def build_sauce(self):
        ...

    def build_topping(self):
        ...


# Concrete Builder
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")

    def build_sauce(self):
        self.pizza.set_sauce("mild")

    def build_topping(self):
        self.pizza.set_topping("ham, pineapple")


# Concrete Builder
class SpicyPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("pan baked")

    def build_sauce(self):
        self.pizza.set_sauce("hot")

    def build_topping(self):
        self.pizza.set_topping("pepperoni, jalapeno")


# Product
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping


# Director
class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder: PizzaBuilder):
        self.builder = builder
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()

    def get_pizza(self):
        return self.builder.pizza


# Client
if __name__ == "__main__":
    waiter = Waiter()

    hawaiian_builder = HawaiianPizzaBuilder()
    spicy_builder = SpicyPizzaBuilder()

    waiter.construct_pizza(hawaiian_builder)
    hawaiian_pizza = waiter.get_pizza()
    print("Hawaiian Pizza:", hawaiian_pizza.dough, hawaiian_pizza.sauce, hawaiian_pizza.topping)

    waiter.construct_pizza(spicy_builder)
    spicy_pizza = waiter.get_pizza()
    print("Spicy Pizza:", spicy_pizza.dough, spicy_pizza.sauce, spicy_pizza.topping)