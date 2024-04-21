# consider these two simple functions:
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return param == "no" and foo() or "no"

# what will this output?
bar(foo())
# bar("yes")

# since param="yes", this means the first expression evaluates to False, meaning foo() never getrs called
# since the result of the and statement where we check param == "no" and foo() does not evaluate to True, Python returns the right side of the expression

