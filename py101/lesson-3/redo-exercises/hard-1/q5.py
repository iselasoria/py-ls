# What do you expect to happen when the greeting variable is referenced in the last line of the code below?


if False:
    greeting = "hello world"

print(greeting)

# solution
# the if block is not executed due to the Fa;se condition and therefore it will not iitialize greeting
# so by the time we try to output it, it will raise a NameError