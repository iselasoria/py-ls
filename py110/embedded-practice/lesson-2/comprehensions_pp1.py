# Consider the following nested dictionary:
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

"""
Compute and display the total age of the family's male members.
Try working out the answer two ways: first with an ordinary
loop, then with a comprehension.

The result should be 444.

"""
# with for loop
male_ages = []

for person in munsters:
    if munsters[person]['gender'] == 'male':
        male_ages.append(munsters[person]['age'])

print(sum(male_ages))

# with list comprehension
all_ages_comprehension = [person['age'] for person in munsters.values()
                          if person['gender'] == 'male']
print(sum(all_ages_comprehension))