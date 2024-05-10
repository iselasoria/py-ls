Implicit coercion often happens as the birpduct of running operations on numeric types.

```python
num1 = 45
num2 = 4
result = num1 / num2 # 11.25
```
In the example above, we take two integers and divide one by the other, but the result is a float.

In the backlgroud, Python coerced the result even though the input as both operands as integers. This happens with numbers that don't have a remainder either:
```python
num1 = 12
num2 = 4
result = num1 / num2 # 3.0
```
If we want to get an integer we must use the integer diviosion [[operators#integer  division]].

This table shows how Python coerces types when performing operations on them.

| Operand 1      | Operand B       | Resulting Type  |
| :-------------:|:---------------:|:---------------:|
| `int`          |      `float`    |     `float`     |
| `int`          |    `Decimal`    |    `Decimal`    |
| `int`          | `Fraction`      |  `Fraction`     |
| `float`        | `Decimal`       |  `--error--`    |
| `float`        | `Fraction`      |  `float`        |
| `Decimal`      | `Fraction`      |  `--error--`    |



Python also implicitly coerces objects into strings when using `print()` so that they may be used as a string.

```python
# unecessary coercion
print(str(3))     # 3
print(str(False)) # False
print(str{4,5,6}) # {4,5,6}

# implicit coercion
print(3)          # 3
print(False)      # False
print([1,2,3])    # [1,2,3]
```
