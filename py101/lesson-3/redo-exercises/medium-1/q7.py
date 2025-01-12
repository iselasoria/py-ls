# One day, Spot was playing with the Munster family's home computer,
# and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# He then ran

mess_with_demographics(munsters)


# Before Grandpa could stop him, Spot hit the Enter key with his tail.
# Did the family's data get ransacked? Why or why not?

# SOLUTION
# dictionaries are mutable objects and therefore, each dictionary in the munsters dicitonary IS
# the original objext taht we are modifying.
