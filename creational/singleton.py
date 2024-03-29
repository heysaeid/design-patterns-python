class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=SingletonMeta):
    pass


if __name__ == "__main__":
    instance1 = MyClass()
    instance2 = MyClass()

    print(id(instance1) == id(instance2))