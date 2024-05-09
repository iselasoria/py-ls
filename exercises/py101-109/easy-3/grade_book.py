"""
Write a function that determines the mean (average) of the three scores passed
to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100. There is no need to check
for negative values or values greater than 100.

I:
three integers

O:
string

Rules:
- calculate average
- Equivalents:
    90 <= score <= 100: 'A'
    80 <= score < 90: 'B'
    70 <= score < 80: 'C'
    60 <= score < 70: 'D'
    0 <= score < 60: 'F'

Alog:
- calculate average of all the scores
- match the average number to the range it falls into and retrieve letter equivalent

"""

def get_grade(first, second, third):
    avg = (first + second + third) // 3

    grade_book = {
        range(90,101) : 'A',
        range(80, 90) : 'B',
        range(70, 80) : 'C',
        range(60, 70) : 'D',
        range(0, 60) : 'F'
    }

    for score, letter_grade in grade_book.items():
        if avg in score:
            return letter_grade

print(get_grade(95, 90, 93)  == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True