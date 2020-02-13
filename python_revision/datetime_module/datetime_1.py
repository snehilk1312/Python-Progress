import datetime
import pytz


dt_utcnow = datetime.datetime.now(tz=pytz.UTC)		# could use 'dt_utcnow=datetime.datetime.utcnow()' too

print(dt_utcnow)

'''
for tz in pytz.all_timezones:
	print(tz)
'''


dt_indnow = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))


print(dt_indnow)


print(dt_indnow.isoformat())

print(dt_indnow.strftime('%B %d, %Y'))


dt_str = 'February 13, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)
