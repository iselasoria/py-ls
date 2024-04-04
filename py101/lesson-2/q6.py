# what will the follwoing code print and why?

def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# there is a variable x pointing to integer 15 in the
# outter scope of the function-- the my_func() function.
# then, one level deeper in the body definition of inner_func1(), there is
# reassignment. Because at this level of scope, the code inside this first nested function does
# still have access to the code in the body of the outter function, we would be accessing that same x and essentially overriding it
# So the first call to print will produce "Inner 1: 25" because we've overriden the original value of 15 by accessing the same variable and overriding it
# the second nested function, inner_func2(),
# does not override or reassign x, it simply make a call to x, which at this level of scope, is still pointing to the integer 15.
# inner_func2() does not have access to the x defined in inner_func1()

