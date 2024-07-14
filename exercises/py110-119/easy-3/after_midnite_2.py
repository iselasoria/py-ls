"""
As seen in the previous exercise, the time of day can be
represented as the number of minutes before or after midnight.
If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour
format, and return the number of minutes before and after
midnight, respectively. Both functions should return a
value in the range 0 through 1439.

You may not use Python's datetime module.

"""

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_string):
    hours, minutes = [int(unit) for unit in time_string.split(':')]
    return ((hours * MINUTES_PER_HOUR) + minutes) %  MINUTES_PER_DAY

def before_midnight(time_str):
    raw_time = MINUTES_PER_DAY - after_midnight(time_str)
    if raw_time == MINUTES_PER_DAY:
        raw_time = 0
    return raw_time


# test cases
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True