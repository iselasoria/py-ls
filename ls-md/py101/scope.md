#fundamentals 
## scope
Scope refers to the availability of variables at different indentation levels.
The rules of scope in python can be remembered (in order) by:
	**LEGB**
		- `local`
		- `enclosing`
		- `global`
		- `built-in`
Python will always try to resolve a variable in the local scope first.

```python
def sample_function(person):
	person = 'Ryan'
	
	if person != 'Ryan':
		print(f'Hey {person}, you\'re not allowed in here!')
	else:
		print(f'Hi {person}, c\'mon in!')

  
  

sample_function('rosa') # Hi Ryan, c'mon in!
```
If it is unable to resolve the variable in the local scope, it will move on to the `enclosing` structure, as is the case with these nested [[functions]]:

```python
def this_is_outter_scope(person):
	person = 'Ryan'
	
	def sample_function(person):
		if person != 'Ryan':
			print(f'Hey {person}, you\'re not allowed in here!')
		else:
			print(f'Hi {person}, c\'mon in!')
	sample_function(person)

this_is_outter_scope('rosa') # Hi Ryan, c'mon in!

```

If it still doesn't find the variable in the enclosing structure, it will look in the `global` scope:
```python
person = 'Ryan'

def this_is_outter_scope(person):
	person = 'Ryan'
	
	def sample_function(person):
		if person != 'Ryan':
			print(f'Hey {person}, you\'re not allowed in here!')
		else:
			print(f'Hi {person}, c\'mon in!')
	sample_function(person)

this_is_outter_scope('rosa') # Hi Ryan, c'mon in!
```

> NOTE: an important thing to note is that Python does _not_ have block scope, so statements like `if` or iterator constructs like `while` loops _**do not**_ create scope.

## `global` keyword

As stated in the `LEGB` rule above, global [[variables]] are available everywhere, for reference. 
However, if we wanted to reassign them, we can't simply do it.
```python
person = 'Rosa'

def sample_function(person):
	person = 'Ryan'
	
	if person != 'Ryan':
		print(f'Hey {person}, you\'re not allowed in here!')
	else:
		print(f'Hi {person}, c\'mon in!')

sample_function(person) # Hi Ryan, c'mon in!

print(person) # Rosa
```
As can be seen above,  line 4 does _not_ reassign the variable `person`, it simply creates a new variable local to the function definition. When we use the same variable name as a global, all we're causing is _**variable shadowing.**_
In order to modify the `global` variable, we must use the [[global]] keyword:
```python
person = 'Rosa'
  
def sample_function(name):
	global person
	person = 'Ryan'
	  
	if name != 'Ryan':
		print(f'Hey {name}, you\'re not allowed in here!')
	else:
		print(f'Hi {name}, c\'mon in!')

sample_function(person) # Hey Rosa, you're not allowed in here!
print(person) # Ryan
```
Now we're talking! As you can see, the call to `print` on the last line actually shows that it points to the string `Ryan`.



Another example:
```python
this_is_global = 'Hi, global variable here'

def scopeinator():
	local_var = 'Hi, I\'m local!'
	print(f'Globals are always available to be referenced anywhere, even from inside this function, as you can see: {this_is_global}')
	print()
	print(f'The vars available inside the function are: {dir()}.')
	
	print(f'Variables local to this function: {locals()}')

scopeinator()
print()
print(dir())
```

