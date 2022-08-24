import datetime
print("current date and time :",datetime.datetime.now())
print("current year :",datetime.date.today().strftime("%y"))
print("month of year:",datetime.date.today().strftime("%B"))
print("week number of the year:",datetime.date.today().strftime("%W"))
print("weekday of the week:",datetime.date.today().strftime("%w"))
print("day of the year:",datetime.date.today().strftime("%j"))
print("day of the month:",datetime.date.today().strftime("%d"))
print("day of the week:",datetime.date.today().strftime("%A"))
print("...................................................mephys date....................................................")





#date time is moDULE
def leap_year(y):
    if y % 400==0:
        return True
    if y % 100==0:
        return False
    if y % 4==0:
        return True
    else:
        return False
print(leap_year(1900))
print(leap_year(2004))
print(leap_year(2074))
print("....................................................................................................")
#date.today -by timedelt
import datetime
today = datetime.date.today()
yesterday= today - datetime.timedelta(days=1)
tomorrow= today + datetime.timedelta(days=1)
print("yesterday : ", yestserday)
print("today:",today)
print("tomorrow:",tomorrow)
print("................................................................................................................................")
def all_sunday(year):
    dt=date(year,1,1)
    print("......................")
    print(dt.weekday())
    dt +=timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)

for s in all_sunday(2020):
    print(s)

print("...................................................................")
from datetime import date, timedelta
def all_sunday(year):
    dt=date(year,1,1)
    print("......................")
    print(dt.weekday())
    dt +=timedelta(days=6 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)

for s in all_sunday(2020):
    print(s)