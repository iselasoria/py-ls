# Alan wrote the following code but Alyssa noticed that this code
# would fail when the input is a negative number, and asked Alan
# to change the loop. How can he make this work? Note that we're
# not looking to find the factors for negative numbers, but we
# want to handle it gracefully instead of going into an infinite loop.

def factors(number):
    divisor = number
    result = []
    while divisor > 0: # used to be !=
        if number % divisor == 0: # the code here checks for wether there is a remainder
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-12))

