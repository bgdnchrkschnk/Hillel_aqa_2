from datetime import datetime, timedelta

now: datetime = datetime.now()
datetime_tomorrow = now + timedelta(days=1, hours=6)
print(datetime_tomorrow)


timedelta_1 = timedelta(days=1, hours=2)

# --------------------


start_time = datetime(year=2022, month=2, day=24)
end_time = datetime(year=2025, month=12, day=27)


def get_timedelta(d1: datetime, d2: datetime) -> timedelta:
    return abs(d2 - d1)


def get_timedelta_seconds(d1: datetime, d2: datetime) -> float:
    return abs(d2 - d1).total_seconds()

result_timedelta = get_timedelta(start_time, end_time)
result_timedelta_seconds = get_timedelta_seconds(start_time, end_time)

print(result_timedelta)
print(result_timedelta_seconds)