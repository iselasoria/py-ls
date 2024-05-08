"""
Write a function that takes a positive integer, n,
as an argument and prints a right triangle whose sides each have n stars.
The hypotenuse of the triangle (the diagonal side in the images below)
should have one end at the lower-left of the triangle,
and the other end at the upper-right.

examples:
triangle(5)
    *
   **
  ***
 ****
*****

triangle(9)
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********

I:
integer

O:
strings on separate lines

Rules:
- n is the length of the sides
- triangle's longest side should have ends at bottom left and top right edges

Algo:
- iterate over the range from 0 to integer
- with each iteration:
    - space is the length of the range minus 1, this leaves space for the top star
    - decrease spaces as you increase stars

"""

def triangle(n):
    spaces = n - 1
    stars = 1

    for idx in range(n):
        print((' ' * spaces) +  ('*' * stars))
        spaces -= 1
        stars += 1


triangle(5)
triangle(9)