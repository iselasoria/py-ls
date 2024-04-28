"""
Create a simple tip calculator. The program should prompt for a bill amount and a tip
rate. The program must compute the tip, then print both the tip and the total
amount of the bill. You can ignore input validation and assume that the user
will enter valid numbers.

example:
What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
"""

def prompt(msg):
    print(f"{msg}")

prompt("What is the bill?")
bill = int(input())

prompt("What is the percentage?")
pct = int(input())

tip_amt = bill * (pct/100)

total = bill + tip_amt

print(f"The tip is ${tip_amt:.2f}, do your total is ${total:.2f}.")