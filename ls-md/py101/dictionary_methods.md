
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

#### `.setdefault()`

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