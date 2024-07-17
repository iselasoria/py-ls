""""
Write a function that takes a string as an argument and returns True if all parentheses in
the string are properly balanced, False otherwise. To be properly balanced, parentheses
must occur in matching '(' and ')' pairs.

I: string
O: Boolean


Rules:
- check that all parentheses int he string are balanced
    - balanced means they appear in matcing pairs, no left overs
    - balances must also mean not starting with a closing parentheses


Model Solution:
What (is) this? --> () --> True
((What) (is this))? -->

DS:
interim: list

Algo:
initialize an open variable to 0
initize a closed varibale to 0

get the index of the first occurence of each open and closed
iterate over the string and each time we find a closed or opened parenthesis, increase acordintly
- if the index of open is smaller than the index of closed and the number of open and closed is the same, return true otherwise false


"""

def is_balanced(str):
    if '(' not in str and ')' not in str:
        return True

    parentheses = 0

    first_open = str.find('(')
    first_closed = str.find(')')

    for ch in str:
        if ch == '(':
            parentheses += 1
        elif ch == ')':
            parentheses -= 1
    print(parentheses)
    return (first_open < first_closed) and parentheses == 0 #! TODO come back and revise the last edge case
# test cases

# print(is_balanced("What (is) this?") == True)        # True
# print(is_balanced("What is) this?") == False)        # True
# print(is_balanced("What (is this?") == False)        # True
# print(is_balanced("((What) (is this))?") == True)    # True
# print(is_balanced("((What)) (is this))?") == False)  # True
# print(is_balanced("Hey!") == True)                   # True
# print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True