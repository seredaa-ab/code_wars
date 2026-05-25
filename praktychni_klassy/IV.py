class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}'s age is {self.age}"

p = Person("john", 34)

print(p.get_info())