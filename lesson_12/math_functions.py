import logging


class CustomMathException(ArithmeticError):
    pass

def add(a: int | float, b: int | float):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise CustomMathException("Only int, float supported!")
    return a + b

def subtract(a: int | float, b: int | float):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise CustomMathException("Only int, float supported!")
    return a - b


def enter_danger_zone():
    logging.warning("Entering Danger Zone")
