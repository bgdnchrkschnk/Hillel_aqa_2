# Визначаємо, які модулі та функції є публічними
from .math_utils import add, subtract
from .string_utils import normalize

__all__ = ["add", "subtract", "normalize"]


print("INIT MESSAGE")