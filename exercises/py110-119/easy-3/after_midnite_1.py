"""
The time of day can be represented as the number of minutes before or after
midnight. If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and
returns the time of day in 24-hour format (hh:mm). Your function should work
with any integer input.

You may not use Python's datetime module.

I: int
O: str

Rules:
- a negative number indicates minutes before midnight
- a positive number indicates minutes after mindnight
- 0 indicates midnight proper
- result should be returned as 24h format --> hh:mm

Model Solution:
-3 ---> three minutes before midnight or three minutes minus 00:00
        24hours minutes the times 3 gets removed from 60, in this case once==> 23
        60 minutes - three minutes --> 57
        formatted ----------> 23:57


DS:
Interim: string, int

Algo:
- initialize min_in_hour = 60
- get total minutes in the day as min_in_hour * hours in day
- subtract input argument from total in day
-
"""

def time_of_day(minutes):
    min_per_hour = 60
    min_per_day = min_per_hour * 24
    print(f"Minutes in a day: {min_per_day}")

    raw_time = minutes % min_per_day
    print(f"Minutes from midnite: {raw_time}")
    raw_time_hh = raw_time // min_per_hour
    print(f"Hours from midnite: {raw_time_hh}.")
    raw_time_mm = raw_time % min_per_hour
    print(f"Minutes from midnite: {raw_time_mm}.")
    return f"{00 + raw_time_hh:02}:{raw_time_mm:02}"

print(time_of_day(0)== "00:00")        # True
print(time_of_day(-3)== "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# data = [[1,2,3], [4,5,6], [7,8,9]]

# result = [[x*2 for x in subilst]for subilst in data]
# #           expression for top_level_iterator in collection
# #           expression for item in top_level_iterator