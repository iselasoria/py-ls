# will the following functions return the same resukts

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

# SOLUTION
# The first function will return `{ prop1: "hi there" }` but the second will return None without throwing errors
# this is due to teh fact that Python will stop immediately after the return statement. Since in this case there is nothing immediately after
# the return statememnt, None will be returned explicitly, the lines below it are unreachable.