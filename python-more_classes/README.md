class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} yemək yeyir.")
class Dog(Animal):
    def bark(self):
        print("Hav hav!")


d = Dog("cubus")
d.eat
print(d.bark)
