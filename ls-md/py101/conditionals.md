Conditionals are used to make decisions based on whether a condition is met or not.
We can use `if` [[statement]]. 
```python
a = 3

if a < 0:
	print(f'{a} is a negative number')
elif a > 0:
	print(f'{a} is a positive number')
else:
	print(f'{a} is zero.')
# 3 is a positive number
```

One common use of conditionals is as breaking points of [[loops]]:
```python
a = 0

while a <= 10:
	print(f'We are counting up to 10: {a}')
	a += 1

# We are counting up to 10: 0
# We are counting up to 10: 1
# We are counting up to 10: 2
# We are counting up to 10: 3
# We are counting up to 10: 4
# We are counting up to 10: 5
# We are counting up to 10: 6
# We are counting up to 10: 7
# We are counting up to 10: 8
# We are counting up to 10: 9
# We are counting up to 10: 10
```
