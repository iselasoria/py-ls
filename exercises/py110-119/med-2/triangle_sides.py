"""
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater
than the length of the longest side, and every side must have a length greater than 0.
If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments
and returns one of the following four strings representing the triangle's
classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

I: three integers
O: srting

Rules:
- valid:
    - sum of two shortest sides must be greater than the 3rd length
    - every side must have a length greater than 0-- any 0? immediately no
- equilateral:
    - all sides the same legnth
- isosceles:
    - two sides are the same, one different
- scalene/;
    - all three sides different

Algo:
- make a list of the three inputs `sides`
- if there are any zeros in input, return 'invalid'
- if the sum of two is less than the third, return invalid
- if the list is unique, then return 'equilateral'
- if the list unique length is 2, then 'isosceles'


"""

def triangle(s1, s2, s3):
    sides = [s1, s2, s3]
    sorted_sides = sorted(sides)

    if 0 in sides or sum(sorted_sides[:2]) <= sorted_sides[-1]:
        return 'invalid'
    elif len(sides) == len(set(sides)):
        return 'scalene'
    elif len(set(sides)) == 1:
        return 'equilateral'
    elif len(set(sides)) == 2:
        return 'isosceles'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 1.5, 3) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True