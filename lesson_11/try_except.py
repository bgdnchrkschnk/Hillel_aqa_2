def divide(a: int, b: int):
    return a / b


# print(
#     divide(5, 0)
# )
# -----------------------------------------------
# try, except, else, finally



# try:
#     print(divide(5, "jbjhbcd"))
# except ZeroDivisionError as e:
#     ...
#     print("Dividing by zero is not possible!")
#     ...
# except TypeError as e:
#     print(f"Types are not appropriate: {e}")
# finally:
#     print("Finally finished")


# try:
#     print(divide(5, "jbjhbcd"))
# except (ZeroDivisionError, TypeError) as e:
#     ...
#     print(f"Something went wrong, {e}")
#     ...
# finally:
#     print("Finally finished")


# try:
#     db_connector = session_db.connect(**config)
#     db_connector.execute("SELECT 1")
#     db_connector.execute("INSERT")
# except ConnectionError as e:
#     print(f"Something went wrong while connecting, {e}")
# finally:
#     db_connector,close()



# def is_adult(age: int):
#     if 18 > age > 0:
#         print(f"Is not adult")
#     elif age <= 0:
#         raise ValueError(f"0 is not valid age")
#     else:
#         print(f"Adult")
#
#
# print(is_adult(-24))


list_of_ages: list[int] = [14, 10, 2, 78, 19]


# try:
#     for age in list_of_ages:
#         is_adult(age)
# except ValueError as e:
#     print(f"ValueError: {e}")
# else:
#     print("No errors in list_of_ages")
# finally:
#     print(f"Reporting saved in db")



# try - спробуй виконати
# except - перехоплюємо помилку
# else - якщо немає помилок - зроби наступне
# finally - зроби наступне в будь якому разі


users = [
    {'name': 'Den', 'math': 50, 'phil': 60},
    {'name': 'Alex', 'math': 50, 'phil': 60},
    {'name': 'Illia', 'math': 50, 'phil': 60},
    {'name': 'Ivan', 'math': 50, 'phil': None},
    {'name': 'Kim', 'phil': 45},
]


def count_marks(users_list: list[dict]):
        for user in users_list:
            try:
                math_mark = user['math']
                phil_mark = user['phil']
                sum_of_marks = math_mark + phil_mark
                print(f"User: {user['name']} has {sum_of_marks} marks in total")
            except TypeError as e:
                print(f"Not valid data for user {user['name']} {e}")
            except KeyError as e:
                print(f"No data about lesson for {user['name']} {e}")
            else:
                print(f"user {user['name']} is VALIDATED successfully")
            finally:
                ...
                print("Total marks was sent via email for user!")




count_marks(users_list=users)






