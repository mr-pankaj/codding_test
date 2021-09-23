from datetime import datetime
import time
import os
import pytz
date_formate = '%Y-%m-%d %I:%M:%S %p %Z%z'
time_formate = '%I:%M:%S %p %Z%z'
london_tz = pytz.timezone('Europe/London')
pacific_tz = pytz.timezone('US/Pacific')
india_tz = pytz.timezone('Asia/Kolkata')
 

# second_datetime = datetime.now(pacific_tz)

# print("UTC Time", datetime.now(pytz.utc).strftime(date_formate))
# print("Indian Time", datetime.now(india_tz).strftime(date_formate))
# print("London Time", first_datetime.strftime(date_formate))
# print("Pacific Time", second_datetime.strftime(date_formate))

# print(dir(datetime.time))

first_start_time = datetime.strptime('2021-09-23 6:30 AM', '%Y-%m-%d %I:%M %p') 
first_start_time = pacific_tz.localize(first_start_time)
first_end_time = datetime.strptime('2021-09-23 3:30 PM', '%Y-%m-%d %I:%M %p')  
first_end_time = pacific_tz.localize(first_end_time)

second_start_time = datetime.strptime('2021-09-23 8:30 AM', '%Y-%m-%d %I:%M %p') 
second_start_time = london_tz.localize(second_start_time)
second_end_time = datetime.strptime('2021-09-23 4:30 PM', '%Y-%m-%d %I:%M %p')  
second_end_time = london_tz.localize(second_end_time)

# print("Pacific Time", first_start_time.strftime(date_formate))
print("UTC Time Start", first_start_time.astimezone(pytz.utc).strftime(date_formate))

print("UTC Time End", first_end_time.astimezone(pytz.utc).strftime(date_formate))

first_end_time

print('======================')

# print("Pacific Time", second_start_time.strftime(date_formate))
print("UTC Time", second_start_time.astimezone(pytz.utc).strftime(date_formate))
print("UTC Time End", second_end_time.astimezone(pytz.utc).strftime(date_formate))


