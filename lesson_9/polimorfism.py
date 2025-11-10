class Animal:

    def make_sound(self):
        if type(self) is Dog:
            print("Woof!")
        elif type(self) is Cat:
            print("Meow!")
        else:
            print("Making sound")

class Dog(Animal):
    ...

class Cat(Animal):
    ...


dog = Dog()
cat = Cat()
dog.make_sound()
cat.make_sound()