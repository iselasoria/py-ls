# given the following simiar snippets of code, what will each code snippet print?

# A
def mess_with_vars(one, two, three):
    one = two # two
    two = three # three
    three = one # two

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Snippet A shows variable shadowing, so even if we change what the variables point to, the variabels in the function are local, so we
# dont actually change the original object
# one is: ['one']
# two is: ['two']
# three is: ['three']

B
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

# Snippet B
# shows variable shadowing, so even if we change what the variables point to, the variabels in the function are local, so we
# dont actually change the original object
# one is: ['one']
# two is: ['two']
# three is: ['three']

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

# Snipet C
# since here we are modifyin the lists, and lists are immutable and passed by reference, we are
# actually changing the original object
# one is: ['two']
# two is: ['three']
# three is: ['one']