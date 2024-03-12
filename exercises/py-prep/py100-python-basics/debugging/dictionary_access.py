"""You are trying to access a value in a dictionary, but the code is giving you an error. 
Can you change line 3 so that it prints "Unknown" instead of raising an error?"""


info = {'name': 'Srdjan', 'age': 38}

print(info['city'])

# solution:
print(info.get('city', 'Unknown'))
# since the key 'city' is not present in the dictionary, we get an error trying to access it
#  we can instead use .get() to get the key when it exists and a default value when it does not