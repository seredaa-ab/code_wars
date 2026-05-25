def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("Invalid class name")

    cls.__name__ = new_name
    return cls

class MyClass:
    pass

class_name_changer(MyClass, "UsefulClass")

print(MyClass.__name__)

class MyClass:
    pass

class_name_changer(MyClass, "1UsefulClass")

print(MyClass.__name__)