# Python Meta Class
A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes.
[Click for more information](https://www.datacamp.com/tutorial/python-metaclasses#:~:text=A%20metaclass%20in%20Python%20is,experience%20working%20with%20Python%20classes.)



# Singleton pattern
A Singleton pattern in python is a design pattern that allows you to create just one instance of a class, throughout the lifetime of a program. Using a singleton pattern has many benefits. A few of them are:
- To limit concurrent access to a shared resource.
- To create a global point of access for a resource.
- To create just one instance of a class, throughout the lifetime of a program.

[Click for more information](https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/)



# Simple Factory Pattern
The design of the Simple Factory Pattern is essentially a creational pattern that provides an interface for creating objects with different types in its subclasses. It also includes a Concrete Factory to manage object creation and selects the appropriate type of objects through input parameters.

The client does not have direct access to the details of object creation and communicates only with the Concrete Factory. Additionally, using this pattern ensures encapsulation, as the details of creation are hidden within the Concrete Factory.



# Factory Method Pattern
The Factory Method design pattern is essentially a creational pattern that provides an interface for creating objects with different types in subclasses. In this pattern, we have abstract product, concrete product, abstract creator, and concrete creator. It also enables us to adhere to the open/closed principle of SOLID.