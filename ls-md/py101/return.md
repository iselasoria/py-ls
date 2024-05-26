#fundamentals

The `return` [[statement]] is used to determine what a [[functions]] will return when called.

```python
  

def name_function(str1, str2):
	return str1 + ' ' +str2

print(name_function('Rosa','Isela')) # Rosa Isela
```

Another example:
```python
def broken_sentence(lista):
	print(lista)
	lista.append('Mullen McMullen')
	return lista

cats = ['Burbus','Gotita','Esmpumita']
print(broken_sentence(cats))
```
The code above shows an [[output]] which is the original list gets printed to the screen. There is also a [[side-effect]], which is the mutation of the list object. Lastly, the return is the newly modified list that still retains its same [[identity]].
