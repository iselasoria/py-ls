#fundamentals 
Built-in methods are simply methods we don't have to import any module in order to use them.

#### `sum()`
The sum built-in function lets us add the contents of  [[collections]]. With a [[list]]:
```python
lst = [5, 9, 3]
suma = sum(lst)

print(suma) # 17
```
With a [[set]]:

```python
s = {4, 3, 1}
suma = sum(s)

print(suma) # 8
```

#### `all()` 
This function lets us iterate through a collection, and if the block returns `True` for every single element, that is, if it mets the specified condition, then the function will return `True`. This also returns `True` if the iterable passed in is empty. That is caused by the fact that there are no elements inside the iterable that would contradict the statement that _all the elements in the collection are truthy_. See [[thruthiness]]
```python
print(all([])) # True 
```

```python
numbers = [2, 4, 6, 8, 10] ^qmki3

# Use all() to check if all elements are even
all_even = all(number % 2 == 0 for number in numbers)

print(all_even)  # This will print True because all numbers are even

```
