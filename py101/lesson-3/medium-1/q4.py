# what does the code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)


# !revise
# this outputs
# 0.8999999999999999
# False
# the reason for this is that Python uses floating point numbers
# for all numeric operations, and these arent precise.
# One work around is to use the math.isclose function from the math module