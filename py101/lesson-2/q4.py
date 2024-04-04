# what will the following print and why?

def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# the call to inner() function on line 10 will print 'Hello World' the comma separated variables will concatenate the strings they reference
# the call to outter() function on line 12 will print'Hello' becase that is all the outter scope has access to in this nested scope scenario
