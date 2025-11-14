from lesson_8.Animal import Animal


class Cat(Animal):

    def __init__(self, name, age, bread, is_alive=True):
        super().__init__(name=name, age=age, is_alive=is_alive)
        self.bread = bread

    def speak(self) -> None:
        print(f"{self} is saying MEOW!..")


slavik = Cat(name='Slavik', age=1, bread="siam")
print(dir(slavik))

slavik.speak()


# slavik.ears = 4
setattr(slavik, "ears", 4)

print(slavik.ears)