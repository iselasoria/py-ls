
# Arithmetic Operators
## `+` Addition
```python
print(4 + 4) # 8
print(38.4 + 41.9) # 80.3
```
## `-` Subtraction
```python
print(80 - 4) # 34
print(48 - 41.5) # -3.5
```
## `*` Multiplication
```python
print(38 * 4) # 152
print(38.4 * 41.1) # 1578.24
```
## `/` Division
Notice that diving two [[integers]] still results in a [[float]]. This is [[implicit_coercion]].
```python
print(16 / 4) # 4.0
print(16 / 2.5) # 6.4
```

## `//`  Integer Division
This operator ensures we get an integer as the result of dividing two integers.

```python
num1 = 12
num2 = 4
result = num1 // num2 # 3
```
If either operand is a [[float]], the result will still be a float but it will be rounded down to a whole number.
```python
print(16 // 2.3) # it resolves to 6.9565 but the // will resolve it as 6.0
```

The `//` operator returns the largest whole number less than or equal; to the floating point result.
## `%` Modulo
This operator returns the `modulous` of a division. Often called the remainder operator, however, there is a mathematical distinction between the nodulous and the remainder when precisely _one_ operand is a negative number.  

```python
print(17 % 3) # 2
```
## `**` Exponentiation
This is used to raise number to the power of some other number.
```python
print(16**3) # 4096
```


# String Operators
## `==` Equality
The `==` equality operator is used to determined whether two values are identiccal.
```python
print(42 == 42)       # True
print(42 == 43)       # False
print('foo' == 'foo') # True (works with strings)
print('FOO' == 'foo') # False (Case matters)
```

Similarly to the `==` another equality operator is `!=` the not equal operator. This operator returns False when two operands _are_ equal to each other and `True` when they _are not_. 
```python
print(42 != 42)       # False
print(42 != 43)       # True
print('foo' != 'foo') # False (works with strings)
print('FOO' != 'foo') # True (Case matters)
```

## `+` String Concatenation
This operator looks like the arithmetic `+` operator but in reality it uses `+` to join two [[strings]]
```python
'1' + '2'
# '12'
'foo' + 'bar'
# 'foobar'
```

## `*` Repetitive String Concatenation
This is used to repeatedly concatenate strings
```python
print('abc' * 3) # 'abcabcabc'
print(3 * 'abc') # 'abcabcabc'
```


# Comparison
Strings are compared _lexicographically_-- character by character from left to right.

# List Operators
## Membership
```python
lst = [4,6,8]
print(7 in lst) # False
print(4 in lst) # True
print(4 not in lst) # False
```

## Concatenation
```python
lst1 = [1,2,3]
lst2 = [4,5,6]
result = lst1 + lst2
print(result) # [1,2,3,4,5,6]
```

## Repetition
```python
lst = [1,2]
result = lst * 2 
print(result) # [1,2,1,2]
```