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