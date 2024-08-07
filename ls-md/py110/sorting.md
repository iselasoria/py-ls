#fundamentals 


## Basic Sorting 
Sorting in Python works by using the comparison operators `<`,  `<=`, `>`, and  `=>` for numbers, and using the Unicode `code point` values for characters.

> ASCII is the American standard and includes 128 unique characters. Unicode, on the other hand, contains characters for virtually every language, with ASCII being the first 128 characters and a subset of the Unicode point values. 

#### Sorting Numbers-- numerical order
```python
sorted([2, 11, 9, 4, 107, 21, 1])
# [1, 2, 4, 9, 11, 21, 107]
```


#### Sorting Strings-- lexicographical order
```python
sorted(['c', 'a', 'e', 'b', 'd'])
# [ 'a', 'b', 'c', 'd', 'e' ]
```

Python goes through character by character to determine which word should come first. If the two elements contain the same characters but one is shorter, like  in the case of `cap` and `cape` in the example above, the shorter string is deemed smaller in the comparison and therefore it gets pushed ahead in the resulting ordered list.*

> `sorted()` returns a new list while `.sort()` mutates the list in place.


#### Sorting in reverse
Both `.sorted()` and `.sort()` accept a `reverse` keyword argument that when set to `True` will sort the list in descending order.

```python
numbers = [2, 11, 9, 4, 107, 21, 1] 
sorted(numbers, reverse=True) #[107, 21, 11, 9, 4, 2, 1]
```

```python
words = ['arc', 'bat', 'cape', 'ants', 'cap'] 
sorted(words, reverse=True) # ['cape', 'cap', 'bat', 'arc', 'ants']
```

---
## Custom Sorting 

#### First-Class and Higher Order Functions
`First-Class Objects` are something you can pass as an argument to a function, something that can be returned as the [[return]] value of [[functions]] and something that can be assigned to a variable or as an element in a data structure (like a list or dictionary).

All the data types we've seen so far meet this condition, but in Python so do functions-- these are called [[first_class_objects]].

Functions that accept or return other functions are known as [[higher_order_functions]].


#### `key` keyword argument 
Both `.sorted()` and `.sort()` accept a `key` keyword that helps in custom sorting. We can pass  a custom function that will essentially use two elements from the iteration and compared them based on the defined rules to decide what gets added in what order. 

**Sorting based on the length of each string**
```python
words = ["apple", "pie", "shortcake"]
sorted_words = sorted(words, key=len)
print(sorted_words)          # ['pie', 'apple', 'shortcake']
```

**Performing case insensitive sorting**
```python
animals = ["Cat", "dog", "ZEBRA", "monkey"]
sorted_animals = sorted(animals, key=str.lower)
print(sorted_animals)     # ["Cat", "dog", "monkey", "ZEBRA"]
```

#### Custom Sorting Example:
Sort the following list by weight first, then by name:

```python
cats = [("Burbus", 9),("Gotita", 8),("Espumin", 7)]
```

We first need the custom function that will determine the ordering. We unpack the [[tuple]] and return in the order we want-- weight, then name:
```python
def weight_then_name(info):
	name, weight = info
	return (weight, name)
```

Lastly, we pass it to the `.sorted()` method:
```python
custom_sorted_cats = sorted(cats, key=weight_then_name)
print(custom_sorted_cats) # [('Espumin', 7), ('Gotita', 8), ('Burbus', 9)]
```

We can add the `reverse` keyword to get the list with the same custom logic, but in descending order:
```python
custom_sorted_cats = sorted(cats, key=weight_then_name, reverse=True)
print(custom_sorted_cats) # [('Burbus', 9), ('Gotita', 8), ('Espumin', 7)]
```