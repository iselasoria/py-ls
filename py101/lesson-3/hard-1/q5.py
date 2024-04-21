# what do you expect to happen when the greeting variable is referenced in the last line of the code below?
if False:
    greeting = "hello world"

print(greeting)

# this will return a NameError. Since the if block is never executed because of the
# condition being false, the varibale greeting is never initialized and so we can't refrence it on the last line
