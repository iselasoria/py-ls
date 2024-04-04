# What will the following code print and why?

num = 5

def my_func():
    num = 10

my_func()
print(num)

# in this case, num is initialzied outside the function.
# then, inside the function definition we have another variable `num`
# but they are not the same num, the second one has local scope, which makes it only available to the
# inside of the function. This is means that the num on line 4 is really a different variable pointing to a separate integer in memory
# Line 6 doesnt print anything because there is no output from the function my_func
# Line 7 outputs 5, because at this level we are only able to access the global num, not the local num defined in the function definition