# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# solution
# it will output False, NaN is not a number, a speical numeric value that indicates taht an operation was intended to return a numbner but failed
# we can use math module:

import math

nan_value = float("nan")

print(math.isnan(nan_value))