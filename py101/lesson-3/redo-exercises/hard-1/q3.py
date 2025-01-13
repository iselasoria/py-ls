# Given the following similar sets of code, what will each code snippet print?

# A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# SOLUTION A-------
"one is: ['one']"
"two is: ['two']"
"three is: ['three] "

# Variable shadowing prevents the reassignments inside the function from affecting the original variables
# ------------------------------------------------------------------------------------

# B
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# SOLUTION B-------
"one is: ['one']"
"two is: ['two']"
"three is: ['three] "
# Again, variable shawdowing pprevents reassignment from affecting the variables outside the function
# ------------------------------------------------------------------------------------

# C
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# SOLUTION C-------
"one is: ['two']"
"two is: ['three']"
"three is: ['one] "
# Contrary to the previous examples, here we are using indexed reassignment so we are in dfact modifying the objkects inside the list

