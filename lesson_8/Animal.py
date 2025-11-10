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