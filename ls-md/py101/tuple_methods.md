#### `.count`
Used to count the presence of an element in the tuple. If not present, `.count()` will return `0`.

```python
this_tup = ('Burbus', 'Gotita','Espumin', 'Burbus')
print(this_tup) # ('Burbus', 'Gotita','Espumin', 'Burbus')

print(this_tup.count('Burbus')) # 2
```

```python
this_tup = ('Burbus', 'Gotita','Espumin')

print(this_tup.count('Clovis')) # 0
```
#### `.index()`
Similar to the [[lists_methods#`.index()`]], this method returns the first index where the argument is found on the calling list.
```python
this_tup = ('Burbus', 'Gotita','Espumin')

print(this_tup.index('Burbus')) # 0
```
```python
this_tup = ('Burbus', 'Gotita','Espumin')
print(this_tup.index('Burbus', 1)) # this raises a ValueError because the argument is not dound from position 1 and up. 
```
### Tuple Unpacking
This is not a method, but rather a concept. One simple use of tuple unpacking is being able to assign values from a tuple to several variables at once:
```python
this_tup = ('Burbus', 'Gotita','Espumin', 'Burbus')

print(this_tup) # ('Burbus', 'Gotita','Espumin', 'Burbus')

print(this_tup.count('Burbus'))
```
> NOTE: although not only made for [[tuple]], unpacking is best used with this data type because it has a reliable number of elements, unlike lists which can be more dynamic.
> The simple rule to remember is that in order to unpack, we must have the same number of variables on the left of the `=` as we do elements in the `tuple`. 
