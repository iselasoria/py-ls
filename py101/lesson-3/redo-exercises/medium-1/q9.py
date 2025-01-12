# consider these two simple functuons:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# what tiwll the following invocation return?

bar(foo())

# SOLUTION
# foo() returns yes, so this is what gets passed to bar()
# this means that inside bar(), param is now "yes" and so
# the return statement now reads True and (foo() or "no")
# this will casue the second part to short circuit. Python determines
# that param == 'yes' and since that is False, the rest of the and statement does not get executed