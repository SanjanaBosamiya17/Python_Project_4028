from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")


d = Dog()
d.sound()

c = Cat()
c.sound()

# this will give error because we cannot create object of abstract class
# a = Animal()
