# file = open("asserts.py", "r")
#
# ...
# print(
#     file.read()
# )
# ...
#
#
# file.close()


try:
    file = open("asserts.py", "r")
    print(file.read())
except BaseException as e: # except
    print(e)
finally:
    if file:
        file.close()

#
with open("asserts.py", "r") as file:
    ...
    print(file.read())
    ...
    ...

import time
#


class Timer:
    def __enter__(self):
        self.start = time.time()
        print("🕒 Початок таймера")
        return self

    def __exit__(self, *args):
        duration = time.time() - self.start
        print(f"⏱ Виконано за {duration:.2f} сек")

with Timer() as t: # Timer() - __enter__,  finally - __exit__
    print("запуск")
