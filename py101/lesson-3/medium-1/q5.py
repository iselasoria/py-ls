# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan"))

# BONUS
# How can you reliably test if a value is nan?

# NaN is a special numeric value that indicated somethign expected to return a number, failed
# you cannot check with ==
# you can use math module to checl for this with math.isnan()
import math

nan_value = float("nan")

print(math.isnan(nan_value))