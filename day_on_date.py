#You are given a date. Your task is to find what the day is on that date.

import datetime as dt
my_date=input()
my_date=dt.datetime.strptime(my_date,'%m %d %Y')
print((my_date.strftime('%A')).upper())
