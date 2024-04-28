"""
Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the odd numbers?
"""

def only_odds():
    tiny_range = list(range(1,100,2))

    for num in tiny_range:
        print(num)

print(only_odds())