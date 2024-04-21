# will the following functions return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# The first function will return the expected dictionary: { prop1: "hi there" }
# but the second function will return None. In Pythoin, if there is nothihgn after the return statement,
# the functio will return None.