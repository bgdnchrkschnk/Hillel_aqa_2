"""
Inheritence
Наслідування дозволяє одному класу (підкласу) переймати властивості
та методи іншого класу (базового).
"""

# class Animal:
#     def speak(self):
#         print("Some sound")
#
# class Dog(Animal):
#     pass

# dog = Dog()
# dog.speak()  # 👉 "Some sound"


"""
Incapsulation
Приховування внутрішніх деталей реалізації — наприклад,
через змінні з префіксом _ або __.
"""
#
# class Animal:
#     def __init__(self, name):
#         self.__name = name  # приватна змінна
#
#     def get_name(self):
#         return self.__name
#
# cat = Animal("Whiskers")
# print(cat.get_name())  # 👉 "Whiskers"

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.__creating_start_balance() # private (no access from the object of class)
        self._type = "classic" # protected (access is True but not recommended)

    def get_balance(self):
        return self.__balance

    def __creating_start_balance(self):
        self.__balance = 0

    def change_balance(self, amount):
        self.__balance += amount





my_account = BankAccount(name="Bohdan")
my_account.change_balance(100)
my_account.change_balance(100)
print(my_account.get_balance())


#
#
#
"""
Polymrphism
Можливість викликати один і той самий метод у різних класах — і він буде працювати по-різному.
"""

# class Animal:
#     def speak(self):
#         pass
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow")
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof")
#
# def make_speak(animal: Animal):
#     if type(animal) == Cat:
#         Cat.speak()
#     elif type(animal) == Dog:
#         Dog.speak()

# barsik = Cat()
# troy = Dog()
#
# make_speak(animal=barsik)
# make_speak(animal=troy)
#
# for animal in (barsik, troy):
#     animal.speak()


"""
Abstraction
Описуємо тільки інтерфейс, а не реалізацію. Зручно через abc (abstract base class):
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        print("SPEAK!")

class Dog(Animal):

    def speak(self):
        print("GAV!")

class Cat(Animal):

    def speak(self):
        print("MEOW!")

barsik = Cat()
troy = Dog()


"""
Метод super() в Python використовується для виклику методів батьківського (базового)
класу з дочірнього (похідного) класу.
Це особливо корисно при наслідуванні, коли потрібно розширити,
а не повністю замінити логіку батьківського класу.
"""