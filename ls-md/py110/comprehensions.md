[[lists]] comprehensions offer a way for us to write iterations with transformations in a simple one-liner.

```python
lst = [2, 4, 6, 8, 10]
doubled_lst = [num * 2 for num in lst]

# [4, 8, 12, 16, 20]
```

## Nested Comprehensions
#### Flattened Result
```python
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result1 = [num * 2 for sublist in lst for num in sublist]
print(result1)
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

# result_storage = [expression with smallest_unit iterable for sublist in main_list for smallest_unit in sublist]
```

#### Retaining Nested Structure
```python
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result2 = [[num * 2 for num in sublist] for sublist in lst]
print(result2)
# [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

# result_storage = [[expression with the smallest_unit iterable for smallest_unit in sublist] for sublist in main_list]
```