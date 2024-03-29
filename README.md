# Design Patterns
In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.

# Types of design patterns
1. Creational: These patterns are designed for class instantiation. They can be either class-creation patterns or object-creational patterns.

2. Structural: These patterns are designed with regard to a class's structure and composition. The main goal of most of these patterns is to increase the functionality of the class(es) involved, without changing much of its composition.

3. Behavioral: These patterns are designed depending on how one class communicates with others.

<hr>


| Creational                        | Description                   |
| -------------                     |:-------------:                |
| Singleton Pattern                         | A Singleton pattern in python is a design pattern that allows you to create just one instance of a class, throughout the lifetime of a program                 |
| Simple Factory Pattern                             | Simple Factory Design provides a centralized mechanism for creating objects, encapsulating the instantiation logic in a separate factory class, allowing clients to create objects without specifying their concrete types directly.
| Factory Method Pattern                             | Factory Method Pattern defines an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created, promoting flexibility and extensibility.
| Abstract Factory Pattern                           | The Abstract Factory design pattern is a creational pattern developed to manage the creation of objects. This pattern allows you to create a group of related objects without the need to instantiate multiple classes. It is typically used when the client is unaware of the exact type of object it needs.
| Builder Pattern                                    | Builder Pattern is a creational design pattern that facilitates the step-by-step construction of complex objects, allowing for flexibility and separation of concerns in the object creation process.
| Prototype Pattern                                  | Prototype Pattern is a creational design pattern that enables copying an object to create new instances, particularly useful when creating objects with similar structures and making slight modifications without starting from scratch each time.



| Structural                        | Description                   |
| -------------                     |:-------------:                |
| Adapter Pattern                                                   | Adapter Pattern is a structural design pattern that facilitates creating an interface between two incompatible interfaces, enabling them to work together without modifying the original code of the classes involved.
| Bridge Pattern                                                   | The Bridge Pattern is a structural design pattern that separates abstraction from implementation using an interface, allowing both to vary independently.
