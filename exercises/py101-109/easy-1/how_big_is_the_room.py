"""
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""
CONVERSION_FACTOR = 10.7639

print("We're going to calculate the area of your livingroom, please enter a width in meters:")
width = int(input())
print("Now we need a legth: ")
length = int(input())

area_sqm= round((length * width), 2)
area_sqft = round((area_sqm * CONVERSION_FACTOR), 2)
print(f"""The area of your livingroom in square feet is: {area_sqft}, and in square meters ir is: {area_sqm}.""")