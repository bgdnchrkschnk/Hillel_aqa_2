from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones


all_timezones = available_timezones()
all_eu_timezones = [tz for tz in all_timezones if tz.startswith("Europe/")]
# print(all_eu_timezones)

# ------------------------------ .astimezone()
datetime_now_kyiv: datetime = datetime.now(tz=ZoneInfo("Europe/Kiev"))
datetime_now_paris: datetime = datetime_now_kyiv.astimezone(tz=ZoneInfo("Europe/Paris"))


# compare date
print(datetime_now_kyiv.date() == datetime_now_paris.date())

# compare time
print(datetime_now_kyiv.time() == datetime_now_paris.time())

# compare timezone
print(datetime_now_kyiv.tzinfo == datetime_now_paris.tzinfo)


# ------------------------------ .replace()

datetime_now_paris_2: datetime = datetime_now_kyiv.replace(tzinfo=ZoneInfo("Europe/Paris"))
print(datetime_now_kyiv)
print(datetime_now_paris_2)


datetime_now_utc: datetime = datetime.now(tz=ZoneInfo("UTC"))
print(datetime_now_utc)


print(datetime_now_kyiv.timestamp())


now = datetime.now()
now.date()

now = now.replace(year=2027,
                  microsecond=0,
            second=0)
print(now)

# replace не конвертує а лише призначає таймзону!