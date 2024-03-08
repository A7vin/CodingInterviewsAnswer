def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    pass


my_class1 = MyClass()
my_class2 = MyClass()

assert my_class1 is my_class2
