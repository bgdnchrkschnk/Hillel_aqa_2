class User:
    def __init__(self, nickname, age, sex):
        self.nickname = nickname
        self.age = age
        self.sex = sex

    def say_hello(self):
        print(f"Hello, i am {self.nickname}, i am {self.age} years old")

    def __del__(self):
        print("__del__ called")
#
#
# # Initialization
# bohdan = User('bgdn', '29', 'male')
#
#
# # Utilization
# bohdan.say_hello()
# bohdan.age=28
#
#
# # Desctruction
#
# bohdan.name = "Bohdan"
# del bohdan
#

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)

    def read_data(self):
        return self.file.read()

    def __del__(self):
        self.file.close()
        print(f"File {self.filename} has been closed.")


# file = open("t.py", mode="r")
# file.read()
# file.close()



file_handler = FileHandler("../t.py", "r")
data = file_handler.read_data()
del file_handler
