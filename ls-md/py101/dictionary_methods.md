#fundamentals 
```python
student = {
	'name' : 'Rosa Isela',
	'surname' : 'Soria',
	'age' : 33,
	'track' : 'ruby',
	'completed_courses' : ['rb101', 'rb109','rb120']
}
```
## `.keys()`
Returns a view object (that can be coerced into a [[lists]]) containing all the keys in the [[dictionary]].
```python

print(student.keys()) # dict_keys(['name', 'surname', 'age', 'track', 'completed_courses'])
print(list(student.keys())) # ['name', 'surname', 'age', 'track', 'completed_courses']
```

## `.values()`

```python
print(list(student.values())) # ['Rosa Isela', 'Soria', 33, 'ruby', ['rb101', 'rb109', 'rb120']]
```

## `.items()`

```python
print(list(student.items())) # [('name', 'Rosa Isela'), ('surname', 'Soria'), ('age', 33), ('track', 'ruby'), ('completed_courses', ['rb101', 'rb109', 'rb120'])]

for k, v in student.items():
	print(f'The key is {k}, and the value is {v}.')
	
# The key is name, and the value is Rosa Isela.
# The key is surname, and the value is Soria.
# The key is age, and the value is 33.
# The key is track, and the value is ruby.
# The key is completed_courses, and the value is ['rb101', 'rb109', 'rb120'].
```

## `.get()`
Attempting to retrieve a key that does not exist will result in `KeyError`:
```python
print(student['study_buddy']) # KeyError
```

We could instead use `.get()` which will retrieve the value at the key if it exists, but return `None` if the key does not exist, instead of causing an error that will break the code.
```python
print(student.get('study_buddy')) # None
```


#### `del`
The delete statement. `del` is used to remove a key value pair from a [[dictionary]].
```python
person = {
	"name": "Deb",
	"age": 30,
	"occupation": "detective",
	"personality": "outgoing"
}

for k, v in person.items():
	print(f"{k} is {v}")
# name is Deb
# age is 30
# occupation is detective
# personality is outgoing

print()

del person["personality"]

for k, v in person.items():
	print(f"{k} is {v}")

# name is Deb
# age is 30
# occupation is detective
```

#### `.get()`
`.get()` lets us retrieve data from a dictionary and return `None` by default when the data does not exists, instead of raising an error like we would by using the retrieve-by-key process.

```python
person = {
	"name": "Debra Morgan",
	"age": 30,
	"occupation": "detective",
	"personality": "outgoing"
}

print(person.get("siblings")) # None
```
We can also pass an optional string argument to return something by default when a key is not found:
```python
print(person.get("siblings", "Dexter Morgan")) # Dexter Morgan
```

#### `.setdefault()`
This method creates a key/value pair if it does not exists:
```python
person.setdefault("city","Miami")

print(person) # {'name': 'Debra Morgan', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'city': 'Miami'}
```
If it does, it won't change the associated value:
```python
person.setdefault("age","35")

print(person) # {'name': 'Debra Morgan', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing'}
```

#### `.pop()`
the dictionary `.pop()` method works by removing the key/value pair that corresponds to the key passed in and returning the value:
```python
just_removed = person.pop("personality")

print(just_removed) # outgoing
print(person) # {'name': 'Deb', 'age': 30, 'occupation': 'detective', 'siblings': 'Dexter Morgan'}
```

#### `.popitem()`
This method allows us to remove the last key/value pair in the dictionary and return it as a [[tuple]]. Although they are _NOT_ [sequences], as of Python 3.7, a [[dictionary]] keeps the order its keys were added in:

```python

# {'name': 'Deb', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'siblings': 'Dexter Morgan'}
print(person.popitem()) # ('siblings','Dexter Morgan')
```

#### `.update()`
This method is called on a dictionary and takes another dictionary (or iterable) as the argument. The result is a modified caller dictionary. 
```python
person = {
	"name": "Deb",
	"age": 30,
	"occupation": "detective",
	"personality": "outgoing",
	"siblings": "Dexter Morgan"
}

places = {
	"work" : "Miami Metro PD",
	"house" : "apartment",
	"name" : "Debra Morgan"
}

  

person.update(places)


print(person) # {'name': 'Debra Morgan', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'siblings': 'Dexter Morgan', 'work': 'Miami Metro PD', 'house': 'apartment'}
print()
print(places) # {'work': 'Miami Metro PD', 'house': 'apartment', 'name': 'Debra Morgan'}
```
> NOTE: Notice how the second dictionary object is left untouched while the calling dictionary gets modified. Also notice that if the key did not exist before, it gets added to the dictionary, and if it did exist already, the value gets overwritten.

#### `|     the merge operator`
The merge operator, `|` works similarly to `.update()` but the difference is using the merge operator returns a _new_ merged dictionary.
```python
person = {

	"name": "Deb",
	
	"age": 30,
	
	"occupation": "detective",
	
	"personality": "outgoing",
	
	"siblings": "Dexter Morgan"

}

  

places = {

	"work" : "Miami Metro PD",
	
	"house" : "apartment",
	
	"name" : "Debra Morgan"
}

print(person) #  {'name': 'Deb', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'siblings': 'Dexter Morgan'}

print()

merged_info_dict = person | places

print(merged_info_dict) # {'name': 'Debra Morgan', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'siblings': 'Dexter Morgan', 'work': 'Miami Metro PD', 'house': 'apartment'}
print()
print(person) # {'name': 'Deb', 'age': 30, 'occupation': 'detective', 'personality': 'outgoing', 'siblings': 'Dexter Morgan'}
```

#### `|=   the update operator 
The update operator works exactly like the method `.update()`
#### `.clear()`
This simply empties the dictionary.