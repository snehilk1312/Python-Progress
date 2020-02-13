import datetime
import pytz

# datetime.date
d=datetime.date(2020,2,1)
tday = datetime.date.today()
print(tday)
print(d)


print(tday.weekday())

print(tday.isoweekday())



timedelta = datetime.timedelta(days=7)

print(tday+timedelta)


print(type(timedelta))

bday=datetime.date(2020, 2 ,14)

till_bday = bday-tday

print(till_bday)


# datetime.time

t= datetime.time(17,52,45,10000)
print(t.hour)


# datetime.datetime

t = datetime.datetime(2020, 2, 13 ,17, 52, 45, 1000)
print(t)
# without 'tz = pytz.UTC' argument dt_today and dt_now
# would output same value, but since we have provided timezone in 
# dt_now , it can differ from dt_today

dt_today = datetime.datetime.today()		#no argument allowed
dt_now = datetime.datetime.now(tz = pytz.UTC)	#argument allowed
dt_utcnow = datetime.datetime.utcnow()		#argument not allowed

print(dt_today)
print(dt_now)
print(dt_utcnow)


# using pytz

dt = datetime.datetime(2020, 2 ,13, 17 , 58,56,100, tzinfo=pytz.utc)
print(dt)
