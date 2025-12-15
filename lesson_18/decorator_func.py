# func decorator

def decorator(func):
    def inner():
        print("Precondition - Do something...")
        func()
        print("POST Condition - Do something...")
    return inner


@decorator
def say_hello():
    print("Hello!")



def decorator_2(func):
    def inner(*args, **kwargs):
        print("Precondition - Do something...")
        func(*args, **kwargs)
        print("POST Condition - Do something...")
    return inner


@decorator_2
def say_hello_name(name: str) -> None:
    print(f"Hello, {name}!")


say_hello_name(name="Bogdan")



# class decorator
class DecoratorUpper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()


# ------------

def decorator_upper_func(func):
    def inner(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        result = result.upper()
        ...
        return result
    return inner


@...
@...
@decorator_upper_func
def return_hello(name):
    return f"Hello World! My name is {name}!"


print(
    return_hello("Bob")
)