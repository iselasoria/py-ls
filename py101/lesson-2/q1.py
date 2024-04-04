# what will the following code print and why?
num = 5

def my_func():
    print(num)

my_func()

# the code will print the integer 5. num variable is
# initialized outside the function definition-- in the global scope
# and therefore it is available to all parts of the code,
# which is why we are able to access it in the print function inside the my_func function definition
