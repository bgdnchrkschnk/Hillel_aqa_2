# LEGB - Local, Enclosing, Global, Built in

str = "global string"

def outer():

    str = "nonlocal string" # enclosing

    def inner():

        str = "local string"

        print(str)

    inner()


outer()