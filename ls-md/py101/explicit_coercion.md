#fundamentals 
The most cmon uses of coercion happen form numbers to string, as in:

```python
num = 578
stringy_num = str(num)
type(stringy_num) # <class 'str'>
```

The `input()` method intakes user input as string, coercion is necessary to make numeric types:

```python
print('How old are you?')
age = int(input())
```
