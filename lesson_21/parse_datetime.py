from datetime import datetime


# --------------------------------- from datetime string to datetime object

date_time_string_1: str = "2024-11-30 17:55:59"
date_time_string_2: str = "24-17-03T5:55:30 PM"
date_time_string_3: str = "28-02-20 8:55:30.255 -0200"


date_time_1: datetime = datetime.strptime(date_time_string_1, "%Y-%m-%d %H:%M:%S")

# print(date_time_1.day)
# print(date_time_1.year)
# print(date_time_1.month)
# print(date_time_1.hour)
# print(date_time_1.minute)
# print(date_time_1.second)
# print(date_time_1.microsecond)
# print(date_time_1.tzinfo)


date_time_2: datetime = datetime.strptime(date_time_string_2, "%y-%d-%mT%I:%M:%S %p")

date_time_3: datetime = datetime.strptime(date_time_string_3, "%y-%m-%d %H:%M:%S.%f %z")

# print(date_time_3.tzinfo)
# print(date_time_3.microsecond)


# --------------------------------- from datetime object to datetime string


date_time_war_end: datetime = datetime(year=2025,
                                       month=12,
                                       day=25,
                                       hour=17,
                                       minute=45,
                                       second=13,
                                       microsecond=123456)

date_time_string_war_end: str = date_time_war_end.strftime("%y-%m-%d %H:%M:%S.%f %z")


print(
    date_time_string_war_end
)