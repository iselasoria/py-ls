"""
Build a program that asks the user to enter the length
and width of a room, in meters, then prints the
room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""

length = float(input('Enter the length of the room: '))
width = float(input('Enter the width of the room: '))

area_meters = length * width
area_feet = area_meters * 10.7639

print(f"The area of the room is {area_meters:.2f} "
      f"square meters ({area_feet:.2f} square feet).")
