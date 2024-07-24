"""
A prime number is a positive number that is evenly divisible only by
itself and 1. Thus, 23 is prime since its only divisors are 1 and 23.
However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12,
and 24. Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and
returns true if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem.
Your task is to programmatically determine whether a number is prime
without relying on functions that already do that for you.

I: int
O: boolean

Rules:
- prime numbers are only divisible by themselves adn by 1
- return wetjer the number is rpime or not

DS:
lists

Algo:
- itereate over the range of 2 (because 1 is the first prime) all the way to the number before the input number
    - with every iteartion
        - check that the input integer is no divisible by each element in the iteartion
        **** primes should have no numbers that they divide nicely into but 1, which is not an option in the iteration and itself, whih is also not an option ****


"""

def is_prime(num):
    if num == 1:
        return False

    return all(num % divisor != 0 for divisor in range(2, num))


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
