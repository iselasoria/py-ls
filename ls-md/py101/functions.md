Functions are snippets of standalone code that can be reused. They are used to break up larger programs into more modular units. They can be defined with or without [[parameters]]. 

By default, a function will return [[None]],  this is called _implicit return_.

```python
def test_function(str1):
	print(str1)

# the return here is None
```

We can use the [[return]] statement to specify the return value.

```python
def test_function(str1):
	return str1 + ' This was added later'

print(test_function('Here is a sentence.')) # The return here is: 'Here is a sentence. This was added later'
```

Functions can be nested too:
```python
def meow():
	print('Meow, meow!')
	
def purr():
	print('Purr, purr')

def happy_cat():
	meow()
	purr()

print(happy_cat())
```
Nested functions make their local variables available to any inner functions. Since inner functions are at the end of the day, functions and as such they define their own [[scope#scope]], [[variables]] defined in the enclosing inner function will not be available to the outer function.


