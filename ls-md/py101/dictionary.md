Dictionaries are non-ordered collections that are composed of `key` /`value` pairs.
```python
student = {
	'name' : 'Rosa Isela',
	'surname' : 'Soria',
	'age' : 33,
	'track' : 'ruby',
	'completed_courses' : ['rb101', 'rb109','rb120']
}
```

We can access values in a dictionary by using a syntax that looks similar to indexed retrieval of elements, but it is not quite the same, as dictionaries are not sequences. Values in dictionaries are accessed via `keys`, not index positions.
```python
student = {
	'name' : 'Rosa Isela',
	'surname' : 'Soria',
	'age' : 33,
	'track' : 'ruby',
	'completed_courses' : ['rb101', 'rb109','rb120']
}

print(student['surname']) # Soria
```

