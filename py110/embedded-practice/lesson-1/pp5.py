"""
Calculate the total age given the following dictionary:
"""
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

age_list = list(ages.values())
total = sum(age_list)
print(total)