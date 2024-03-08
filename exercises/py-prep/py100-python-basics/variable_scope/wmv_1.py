# what will the following code do and why?
if True:
    my_value = 20

print(my_value)

# this code will print 20. SInce the condition is always true, the my_value variable gets initiated and set to 20. 
# by the time we reach the last line, the my_value variable is still in scope. In Python, when a variable is
# initialized inside a block ( as is the case with this if statement), that variable is still available and in scope outside the block


