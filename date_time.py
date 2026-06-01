# The date and time objects are im-mutable.

import datetime
birthday = datetime.date(2026, 05, 18)
print(birthday)  # Syntax Error (the zero behind the month's number is not required)

import datetime
birthday = datetime.date(2026, 5, 18)
print(birthday)  # 2026-05-18

print(type(birthday))  # 2026-05-18 <class 'datetime.date'>

import datetime
today = datetime.date.today()
print(today)  # 2026-05-18

# Time follows the 24 hour format.

import datetime
start = datetime.time()
print(start)  # 00:00:00
print(type(start))  # <class 'datetime.time'>

import datetime
start_hour = datetime.time(hour = 6, minute = 45, second = 3)
print(start_hour)  # 06:45:03

# The zero behind the hour's / minute's / second's number is not required.
# Also, positional / keyword arguments could be provided.

# datetime object:

import datetime
start_date_time = datetime.datetime(2001, 3, 15)
print(start_date_time)  # 2001-03-15 00:00:00

import datetime
start_date_time = datetime.datetime(2001, 3, 15, 23, 15, 25)
print(start_date_time)  # 2001-03-15 23:15:25

import datetime
today = datetime.datetime.today()
print(today)  # 2026-05-18 08:11:00.490859
now = datetime.datetime.now()
print(now)  # 2026-05-18 08:11:00.490891

print(today.year)  # 2026
print(today.month)  # 5
print(today.day)  # 18

print(now.hour)  # 8
print(now.minute)  # 11
print(now.second)  # 0

# weekday(): It starts from Monday with a value as 0.

import datetime

today = datetime.datetime.today()
print(today)  # 2026-05-18 08:13:04.568160
print(today.weekday())  # 0

# replace(): It creates a new date (no mutation in the current one as it’s im-mutable) of the already created with an updated data.

import datetime
today = datetime.datetime.today()
print(today)  # 2026-05-18 08:17:09.756789

another_month = today.replace(month = 1)
print(another_month)  # 2026-01-18 08:17:09.756789

# strftime:

import datetime
today = datetime.datetime.today()

print(today.strftime("%m"))  # 05
print(today.strftime("%d"))  # 18

print(today.strftime("%Y"))  # 2026
print(today.strftime("%y"))  # 26

print(today.strftime("%d-%m-%Y"))  # 18-05-2026

print(today.strftime("%A"))  # Monday
print(today.strftime("%B"))  # May

# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
# from datetime import date, time, datetime
# some_date = datetime.date(2002, 2, 22)
# some_time = datetime.time(9, 45, 23)
# one_from_two(some_date, some_time)  # => datetime object representing 2002-02-22 09:45:23

import datetime

def one_from_two(some_date, some_time):
    year = some_date.year
    month = some_date.month
    day = some_date.day
    
    hour = some_time.hour
    minute = some_time.minute
    second = some_time.second
    
    return datetime.datetime(year, month, day, hour, minute, second)

# timedelta: To get the time duration (Eg: movie running time).

import datetime
birthday = datetime.datetime(2001, 3, 15, 23, 14, 25)
current_time = datetime.datetime.today()

current_age = current_time - birthday
print(f"Current age in days with time: {current_age}")  # Current age in days with time: 9194 days, 14:06:34.443220
print(type(current_age))  # <class 'datetime.timedelta'>
print(f"Current age in seconds: {current_age.total_seconds()}")  # Current age in seconds: 794412394.44322

seven_hundred_days = datetime.timedelta(days = 700, hours = 12)
print(f"\nTimedelta: {seven_hundred_days}")  # Timedelta: 700 days, 12:00:00
print(seven_hundred_days * 2)  # 1401 days, 0:00:00

print(f"\nAddition of seven_hundred_days to current date: {current_time + seven_hundred_days}")  # Addition of seven_hundred_days to current date: 2028-04-18 01:20:59.443220


