#fundamentals 

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

