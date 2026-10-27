class Animal:
    pass
class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("BOW BOW!!")

d=Dog()
d.bark()