#fundamentals 
## `len()`
The `len()` method can be used to determine the list of a collection, such as a [[lists]].

```python
cats = ['Burbus','Gotita','Espumin']

print(len(cats)) # 3
```

## `append()`
`append()` is used to mutate a list by adding an element to the end of it:

```python
cats = ['Burbus','Gotita','Espumin']
cats.append('Mullen McMullen')

print(len(cats))  # 4
print(cats) # ['Burbus', 'Gotita', 'Espumin', 'Mullen McMullen']
```

## `pop()`
`pop()` is a mutating method that removes the element at the specified index. By default it will use `-1` which will remove the last element in the list.
This method returns the element it just removed from the list.

```python
cats = ['Burbus','Gotita','Espumin']
print(id(cats)) # 140485531729024
print(cats.pop()) # Espumin
print(cats) # ['Burbus', 'Gotita']
print(id(cats)) # 140485531729024
```

## `reverse()`
This method reverses a list. It returns `None`, it simply mutates the list it gets called on.
```python
cats = ['Burbus','Gotita','Espumin']

print(cats)  # ['Burbus','Gotita','Espumin']
cats.reverse()
print(cats) # ['Espumin', 'Gotita', 'Burbus']
```

## `extend()`
The `extend()` method takes two lists and modifies the calling list to inclide the elements from the second list.

```python
a = [3,5,7]
b = [4,2,0]

print(f"{a} and id: {id(a)}")
print()

print(f"{b} and id: {id(b)}")

a.extend(b)
print(f"List a is now: {a}, and id: {id(b)}")


# [3, 5, 7] and id: 140214653709120

# [4, 2, 0] and id: 140214653707072
# List a is now: [3, 5, 7, 4, 2, 0], and id: 140214653707072
```

## `insert()`
The `.insert()` method allows you to insert an element into an existing list.

```python
a = [3,5,7]

print(f"{a} and id: {id(a)}")

a.insert(1, "hi")
print(a)
print(f"{a} and id: {id(a)}")

# [3, 5, 7] and id: 139912383293632
# [3, 'hi', 5, 7]
# [3, 'hi', 5, 7] and id: 139912383293632
```

#### `.remove`
`.remove()` will remove from the list the element that we pass as an arugment. This is a mutating method.

```python
a = ['rosa','isela','soria','monzon']

a.remove('isela')
print(a)

['rosa', 'soria', 'monzon']
```

#### `.clear()`
This method will mutate the caller by removing all the elements it contains-- clearning the list.
```python
a = ['rosa','isela','soria','monzon']
print(a) # ['rosa', 'isela', 'soria', 'monzon']
print(id(a)) # 140333675799360

a.clear()

print(a) # []
print(id(a)) # 140333675799360
```

#### `.index()`
This method will return the index of the **_first_** occurence of the argument in the caller:
```python

a = ['rosa','isela','soria','monzon', 'soria']
print(a.index('soria')) # 2
```

Idex can also take a start and stop:

```python
a = ['rosa','isela','soria','monzon', 'avila','soria',"soria","monzon"]

print(a.index('soria')) # 2

print(a.index("soria",3,6)) # 5
```

#### `.count()`
This method will count the occurrences of an element in a list:
```python
lst = ["dog","cat","bird","cat", "bear","cat"]

cats_ct = lst.count("cat")
print(cats_ct)
```

#### `.copy()`
Copy creates a shallow copy of the list
```python
a = ['rosa','isela','soria','monzon', 'avila','soria',"soria","monzon"]

print(id(a)) # 140457789433664
b = a.copy()
print(id(b)) # 140457789431296
```
> NOTE: when working with shallow copies, the nested elements in the collection are shared.
> 
```python
a = ['rosa','isela','monzon', ['avila','garcia'],'soria',"monzon"]

b = a.copy()
print()

b[3][1] = 'GARCIA'
print(b)
	
['rosa', 'isela', 'monzon', ['avila', 'GARCIA'], 'soria', 'monzon']
```
> NOTE: Nested elements are NOT shared when using `.deepcopy()`
```python
import copy

a = ['rosa','isela','monzon', ['avila','garcia'],'soria',"monzon"]

b = copy.deepcopy(a)

print(a) # ['rosa', 'isela', 'monzon', ['avila', 'garcia'], 'soria', 'monzon']
print(b) # ['rosa', 'isela', 'monzon', ['avila', 'garcia'], 'soria', 'monzon']

a[3][1] = "GARCIA"

print(a) # ['rosa', 'isela', 'monzon', ['avila', 'GARCIA'], 'soria', 'monzon']
print(b) # ['rosa', 'isela', 'monzon', ['avila', 'garcia'], 'soria', 'monzon']
```
There isn't anything we can do to one that would be seen in the other.

#### `.sort()`
`.sort()`  is a mutating method that sorts elements in the list in lexicographic order for [[strings]] and in numerical order for [[numbers]] types.
```python
>>> numbers = [61, 103, 525, 10100, 25, 3]
>>> numbers.sort()
>>> numbers
[3, 25, 61, 103, 525, 10100]
```

```python
>>> animals = ['cat', 'aardvark', 'horse', 'python', 'orangutan'] >>> animals.sort() >>> animals ['aardvark', 'cat', 'horse', 'orangutan', 'python']
################################
>>> numbers = ['61', '103', '525', '10100', '25', '3'] >>> numbers.sort() >>> numbers ['10100', '103', '25', '3', '525', '61']
```

This method relies on the ability to check a > b, and as long as that is checkable, the method will work. But you can't compare [[integers]] to [[strings]] for example.

You can, however, make use of the `key` to pass in a function:
```python
>>> numbers = ['61', '103', 525, '10100', '25', '3']
>>> numbers.sort(key=str)
>>> numbers
['10100', '103', '25', '3', 525, '61']
```

`.sort()` also takes in an optional argument `reverse` which we can use to choose between the default `False` to sort in ascending order, or overwrite it with `True` to get the list sorted in descending order. 
#### `.reverse()`
Besides using sort, we can also use `.reverse()` to reverse the order of a list. 
```python
a = ['michael','carlyle','hall']

a.sort(reverse=True)

print(a) # ['michael', 'hall', 'carlyle']
```
The difference between using reverse and sorting with reverse is that `.reverse()` retains the order, just swaps the elements and `sort()` with a `reverse=True` will sort lexicographically, and _then_ reverse.

```python
a = ['michael','carlyle','hall']

a.reverse()

print(a) # ['hall', 'carlyle', 'michael']
```