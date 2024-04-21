# what is the output of the following code?
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# SOLUTION
# this outputs 34.
# the function definition returns the argument passed in plus 8, so the function would return 50
# the value that the variable new_answer points to is 50, But since integers are imutable in Python, this
# means that when we add, we are just pointing to a new integer object in memory
# for this reason, when we go to use the value that answer variable points to, we are still directed to 42
# and thus subtracting 8 from that yields 35
