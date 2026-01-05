from time import sleep
from datetime import datetime, date, time


def print_greeting(delay=0):
    sleep(delay)
    print("Hello my friend!")

#
# print_greeting(delay=10)

now: datetime = datetime.now()
# print(now)
#
# print(
#     now.tzinfo)

dt: datetime = datetime(year=2025, month=12, day=25, hour=17, minute=45, second=13)
d: date = date(year=2025, month=12, day=25)
t: time = time(hour=17, minute=45, second=13)

print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
# -----------------
print(d.day)
print(d.year)
print(d.month)
# -----------------
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)



date_from_datetime: date = dt.date()
time_from_datetime: time = dt.time()

print(date_from_datetime)
print(time_from_datetime)