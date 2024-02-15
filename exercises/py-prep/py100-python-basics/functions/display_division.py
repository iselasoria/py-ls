# wihtout running, what will this print?

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

# as it is, nothing will be printed because the function is defined but never invoked
# to invoke the function we need to call it like: multiples_of_three()