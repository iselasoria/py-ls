"""
The Fibonacci series is a sequence of numbers in which each number is
the sum of the previous two numbers. The first two Fibonacci numbers
are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3,
the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on.
In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

I: int
O: int

Rules:
- each number in the sequence is the sum of the previous two numbers
- starts with the first two numbers being 1 and 1

Model Solution:
starting ==> 1 and 1
third --> 1 + 1 = 2
fourth -> 1 + 2 = 3
fifth --> 2 + 3 = 5
sixth --> 3 + 5 = 8


DS:
list

Algo:
- start with a list of 1 and 1 first and second

- starting from the number 3 (since we have the first two)
    - iterate  all the way up to the input integer
    - first and second get reassigned to first being now last, and last being first plus last
- return the variable last
"""

def fibonacci(num):
    leading, trailing = [1, 1]

    for i in range(3, num + 1):
        leading, trailing = [trailing, leading + trailing]

    return trailing



# test cases
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True