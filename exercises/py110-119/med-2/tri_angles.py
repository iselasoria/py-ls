"""
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees,
and every angle must be greater than 0. If either of these conditions is
not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments
and returns one of the following four strings representing the triangle's
classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have
to worry about floating point errors. You may also assume that the
arguments are in degrees.

I: int
O: string

Rules:
- right: one angle is 90
- acute: all three angles are under 90
- obtuse: one angle is greater than 90
- invalid:
    - sum of all angles must be 180 exactly
    - every angle must be greater than 0


DS:
lists

Algo:
- init 'angles' list with the three args

- if 0 is in the list or if the sum is not exaqctly 180, return invalid

- sort the sides
- if the last element(the largest) is greater than 90, then 'obtuse'
- if any angle is 90, right
- if all angles are under 90, acute
"""
def triangle(a1,a2,a3):
    angles = [a1, a2, a3]
    angles.sort()

    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    elif angles[-1] > 90:
        return 'obtuse'
    elif 90 in angles:
        return 'right'
    elif all(angle < 90 for angle in angles):
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True