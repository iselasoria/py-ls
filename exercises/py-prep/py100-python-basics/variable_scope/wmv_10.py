# what will the code do and why?
b = [1, 2, 3]

def my_function():
    b[0] = 10

print(my_function())
print(b)


# global variable b is initialzed and set to the lsit object  [1, 2, 3]
# the function definition then references the object referenced by global b and reassigns the first element to 10
# this example shows that lists are mutbale objects, adn they can be modified from within a fucntion
# b is not  alocal variable in the function (we are not reassigning) and thus, we are acting on the global b