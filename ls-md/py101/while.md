#fundamentals while loops rely on [[conditionals]] to know how many times to execute the block. It will execute for as long as the conditional returns `True`. This type of iterations rely on an index and counter that must be changed so that at some point the [[thruthiness]] of the condition will return a falsy value.

```python
counter = 0

while counter <= 10:
	print('Still under 10, mate!')
	counter += 1
print(f'Your counter is at {counter}; reached over 10 and the condition returned falsey, so now you are outside the loop again.')
```