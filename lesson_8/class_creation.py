# class Animal:
#     ...
#
#
# barsik = Animal()
# troy = Animal()
# slavik = Animal()
#
# -----------------------

# class Animal:
#     head = 1
#     eyes = 2
#
# barsik = Animal()
# troy = Animal()
# slavik = Animal()


# print(barsik.head)
# print(troy.head)
# print(slavik.head)


class Animal:

    head = 1
    eyes = 2

    def __init__(self, name: str, age: int, is_alive: bool = True):
        self.name = name
        self.age = age
        self.is_alive = is_alive

    def move(self) -> None:
        print(f"{self} is moving..!")


    def speak(self) -> None:
        print(f"{self} is speaking..")


barsik: Animal = Animal(name="barsik", age=1)
troy: Animal = Animal(name="troy", age=5)
slavik: Animal = Animal(name="slavik", age=2)

print(barsik.head, barsik.name, barsik.age, barsik.is_alive)
print(troy.head, troy.name, troy.age, troy.is_alive)
print(slavik.head, slavik.name, slavik.age, slavik.is_alive)

print(type(troy) == Animal)
print(barsik)

troy.move()
barsik.speak()

