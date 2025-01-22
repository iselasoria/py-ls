"""
Create a simple tip calculator. The program should prompt for a bill
amount and a tip rate. The program must compute the tip, then print
both the tip and the total amount of the bill. You can ignore input
validation and assume that the user will enter valid numbers.

EXAMPLE:
What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
"""

bill = float(input('What is the bill amount? '))
rate = float(input('What is the tip rate? '))

tip = bill * (rate / 100)
total = bill + tip

print(f"The tip is ${tip}")
print(f"The total is ${total}")