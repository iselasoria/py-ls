# Print all even numbers from 1 to 99, inclusive,
# with each number on a separate line.

# Bonus Question: Can you solve the problem by
# iterating over just the even numbers?
def odd(n):
    return n % 2 != 0


for num in range(1, 100):
    if odd(num):
        next
    else:
        print(num)