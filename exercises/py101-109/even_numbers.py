"""
Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

Bonus Question: Can you solve the problem by iterating over just the even numbers?
"""

def only_even():
    lista = list(range(2,100,2))
    for num in lista:
        print(num)

only_even()