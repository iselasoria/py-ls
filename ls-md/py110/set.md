#fundamentals 

Sets are [[collections]] with the following qualities:
1.  unordered
2.  mutable
3.  unique

The fact that they're unique makes them very efficient for checking membership-- in the case of lists, we'd have to iterate over every single element, including duplicates, which may take a while if there are many.


There is no such thing as an empty literal set; we'd have to use `set()`

```python
my_set = {}
print(type(my_set)) # THIS IS ACTUALLY AN EMPTY DICTIONARY!!!
```

```python
my_set = set(2,4,6)
print(type(my_set)) # now THIS is a set!
```