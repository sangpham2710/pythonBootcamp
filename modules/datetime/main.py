import datetime
mytime = datetime.time(13, 20, 1, 20)
print(mytime)

today = datetime.date.today()
print(today)
print(today.ctime())
mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1, 20)
mydatetime.replace(year=2022)
print(mydatetime)

d1 = datetime.date(2020, 11, 3)
d2 = datetime.date(2019, 11, 3)
result = d1 - d2
print(result)
