#fundamentals 
Mutability refers to whether an object can be changed. 
Mutable date types such as [[lists]], [[dictionary]], or [[set]], can be altered in place.
When we change mutable objects, we are altering their state but we are not changing their [[identity]].

```python
student = {
	'name' : 'Rosa Isela',
	'surname' : 'Soria',
	'age' : 32,
	'track' : 'ruby',
	'completed_courses' : ['rb101', 'rb109','rb120']
}

print(student) # {'name': 'Rosa Isela', 'surname': 'Soria', 'age': 32, 'track': 'ruby', 'completed_courses': ['rb101', 'rb109', 'rb120']}
print(id(student)) # 140479859354176

student['age'] = 33

print(student) # {'name': 'Rosa Isela', 'surname': 'Soria', 'age': 33, 'track': 'ruby', 'completed_courses': ['rb101', 'rb109', 'rb120']}
print(id(student)) # 140479859354176
```
As can be seen above, the object we modified retains its original [[identity]], it has been mutated.

For objects that are immutable, meaning once they are set, they cannot be changed, include [[strings]], [[integers]] and [[tuple]] to name a few. 

```python
name = 'Rosa Isela'
print(id(name)) # 140717163365808

name = name + ' Soria' 
print(id(name)) # 140717176241280
```
As seen above, any attempt to alter the string will simply result in a brand new string object with a new [[identity]].

Another example:
```python
def change(string):
    new_str = ''
    print(f'Object ID when empty: {id(new_str)}')
    for char in string:
        new_str += char
        print(f'Object ID after populated: {id(new_str)}.')
        return new_str
change('Burbus')
```

