# Абстрактний клас тварини
from abc import abstractmethod, ABC


class Animal(ABC):

    @abstractmethod # клас стає абстрактним
    def make_sound(self):
        ...


    def go_to_sleep(self):
        print("Sleeping...")


# Клас собаки, що успадковує абстрактний клас Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Клас кота, що успадковує абстрактний клас Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Rabbit(Animal):
     def make_sound(self):
         return "PFfff!"

animals = [Dog(), Cat(), Rabbit()]

for animal in animals:
    print(animal.go_to_sleep())


# --------------------------------------------------------------------------

class DBCursor(ABC):

    @abstractmethod
    def select(self, query):
        ...

    @abstractmethod
    def mutation(self, query):
        ...

    @abstractmethod
    def create_user(self, user):
        ...

class PostgresCursor(DBCursor):
    def select(self, query):
        print(query)

    def mutation(self, query):
        print(f"mutation: {query}")

    def create_user(self, user):
        print(f"create_user: {user}")

class SQLiteCursor(DBCursor):
    def select(self, query):
        print(query+"LITE")

    def mutation(self, query):
        print(f"SQLITE mutation: {query}")

    def create_user(self, user):
        print(f"SQLITE create_user: {user}")

