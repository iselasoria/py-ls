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