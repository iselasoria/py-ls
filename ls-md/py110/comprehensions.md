#fundamentals 
Comprehensions offer a way for us to write iterations with transformations in a simple one-liner. Although helpful, they can be overused or used inappropriately, like with a [[print]] statement:
```python
nums = [1, 2, 3, 4, 5]
[print(num) for num in nums if num % 2 != 0] # [None, None, None]
```
> The basic rule to remember is, _don't_ use comprehensions if you don't want to use the return values.


---
---

#### `List Comprehensions`
[[lists]]

**Basic Anatomy**
`[output_expression for item in existing_list if condition]`
```python
lst = [2, 4, 6, 8, 10]
doubled_lst = [num * 2 for num in lst]

# [4, 8, 12, 16, 20]
```

####  `Set Comprehensions`
[[set]]

**Basic Anatomy**
`{output_expression for item in existing_list if condition}`

```python
nums = [1, 1, 2, 3, 4, 4, 5]
distinct_squares = {num**2 for num in nums}
print(distinct_squares)  # {1, 4, 9, 16, 25}
```
> NOTE: Because of the unique element nature of [[set]],  it is possible to end up with fewer  elements than in the initial collection. 


#### `Dictionary Comprehensions`
[[dictionary]]

**Basic Anatomy**
`{key_expression: value_expression for item in existing_list`
                                `if condition}`
```python
fruits = ['apple', 'banana', 'cherry']
fruit_length = {fruit: len(fruit) for fruit in fruits}
print(fruit_length)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

---

## Nested Comprehensions
[[nested_data]]

**Basic Anatomy**
`[output_expression for sublist in outer_list
                   `if condition1
                   `for item in sublist
                   `if condition2]`
                   


```python
import random

cities = ['London','Los Angeles','CDMX','Cape Town', 'Manila','Sydney']

weekly_forecast = {city: [random.randint(50,90) for _ in range(8)] for city in cities}

print(weekly_forecast)
# {
	# 'London': [54, 66, 58, 65, 64, 58, 63, 73],
	# 'Los Angeles': [88, 65, 67, 88, 71, 60, 59, 53],
	# 'CDMX': [71, 77, 81, 62, 61, 83, 62, 90],
	# 'Cape Town': [89, 53, 77, 65, 51, 66, 56, 65],
	# 'Manila': [64, 90, 51, 61, 81, 62, 90, 86],
	# 'Sydney': [79, 75, 84, 63, 54, 65, 59, 65]
# }
```


---
### More examples of nested iteration

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

