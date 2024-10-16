import time
import datetime
import calendar

# Returns the formatted time
print(time.asctime(time.localtime(time.time())))
print("\n")

# Returns the current datetime object
print(datetime.datetime.now())
print("\n")

# Returns the datetime object for the specified date
print(datetime.datetime(2024, 4, 4))
print("\n")

# Returns the datetime object for the specified time
print(datetime.datetime(2024, 4, 4, 1, 22, 50))
print("\n")

# Printing the calendar of September 2024
cal = calendar.month(2024, 9)
print(cal)
print("\n")
