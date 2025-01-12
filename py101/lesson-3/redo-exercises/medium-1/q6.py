# what is the output of this code:

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# SOLUTION
# numbers are immutable in python. Here we pass the integer 42 and the mess_with_it() function
# takes 43 and adds 8 which yields 50. This is the return of the funciton, but we have not altered the original number that answer points to
# on line 10 when we use answer and take away 8, we are starting with integer 42 so that line prints 50
