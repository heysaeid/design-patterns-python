# Singleton pattern
A Singleton pattern in python is a design pattern that allows you to create just one instance of a class, throughout the lifetime of a program. Using a singleton pattern has many benefits. A few of them are:
- To limit concurrent access to a shared resource.
- To create a global point of access for a resource.
- To create just one instance of a class, throughout the lifetime of a program.

[Click for more information](https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/)


# Python Meta Class
A metaclass in Python is a class of a class that defines how a class behaves. A class is itself an instance of a metaclass. A class in Python defines how the instance of the class will behave. In order to understand metaclasses well, one needs to have prior experience working with Python classes.
[Click for more information](https://www.datacamp.com/tutorial/python-metaclasses#:~:text=A%20metaclass%20in%20Python%20is,experience%20working%20with%20Python%20classes.)

# Factory Method
The Factory Method pattern is a creational design pattern that provides an interface for creating objects, but allows subclasses to decide which class to instantiate. This allows the creation of objects to be decoupled from their usage, so that the code that uses the objects does not need to know the specifics of how they are created.

The Factory Method pattern is useful when you need to create objects based on some input or condition. By delegating the creation of objects to a factory class or method, you can keep the creation logic separate from the rest of the code, which makes the code easier to maintain and test.