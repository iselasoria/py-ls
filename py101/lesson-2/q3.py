# what will the following print and why?
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# since we use the global keyword inside the funtion definition
# before referencing the num variable, we now have
# access to the num variable defined in the gloabl scope. This means that in the next line,
# line 6, we are reassigning the num variable from integer 5 to integer 10
# and thus when we print the num, the variable is referencing the integer 10