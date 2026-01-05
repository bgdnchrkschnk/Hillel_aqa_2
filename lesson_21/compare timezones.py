from datetime import datetime
from zoneinfo import ZoneInfo

tran_tbilisi = datetime(year=2025, month=12, day=27, hour=1, minute=15, second=45, tzinfo=ZoneInfo("Asia/Tbilisi"))
day_of_tran_kyiv = tran_tbilisi.astimezone(ZoneInfo("Europe/Kiev"))
now = datetime.now(tz=ZoneInfo("Europe/Kiev"))


if day_of_tran_kyiv.date() == now.date():
    print("Put transaction into payout!")
else:
    print("Make bill tomorrow!")
