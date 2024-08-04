#fundamentals 
There are a few statements we can use in iteration that allow us to better control it.
#### `continue`
The `continue` statement allows us to skip over to the next iteration. 
```python
for i in range(10):
	if i % 2 == 0:
		print(f"I'm {i} and I'm getting skipped because I'm even")
	continue

print(i)

# I'm 0 and I'm getting skipped because I'm even
# 1

# I'm 2 and I'm getting skipped because I'm even
# 3

# I'm 4 and I'm getting skipped because I'm even
# 5

# I'm 6 and I'm getting skipped because I'm even
# 7

# I'm 8 and I'm getting skipped because I'm even
# 9
```
This snippet of code uses `continue` to skip to the next item in the range if the number is even. The print in the outter block catches all the numbers that are odd.
#### `break`
`break` is used when we want to force an iteration to end. The code snippet below has a range from `0` to 9 `but forces the break at `5`.
```python
for i in range(10):
	if i == 5: 
		break
	print(i)
# 0
# 1
# 2
# 3
# 4

```
#### `else`
Here `else` serves as a catch-all statement; if we add a break inside the [[for]] loop,  the `else` statement would not execute. 
```python
for i in range(5):
	print(i)
	# if i == 3:
		# break
else:
	print("Loop completed without break")
# 0
# 1
# 2
# 3
# 4
# Loop completed without break
```

