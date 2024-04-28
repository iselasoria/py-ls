# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

def odd_innit(num):
    return (abs(num) % 2) != 0

print(odd_innit(14))
print(odd_innit(10))
print(odd_innit(17))