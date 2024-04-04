# what will the following code do?

def my_func():
    num = 10

my_func()
print(num)

# in this code snipet, there is no variable num defined in the global scope.
# Inside the function definition there is a variable num, but this is local scope
# since the function does not have a call to the print method, nothing will be
# output by the call to my_func on line 6.
# when we go to call print on variable num, we'll get a NameError error
# because num is a local variable and is unavailable to the code beyond the
# body of the function where it was defined
