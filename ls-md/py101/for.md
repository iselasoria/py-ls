`for` loops iterate over a sequence such as [[lists]], [[strings]], [[tuple]] or [[range]]. The big benefit is you don't have to worry about indexing the runs or increasing a counter, they iterate for the number of elements in the [[collections]], unlike the [[while]] [[loops]] which rely on  [[conditionals]].

`list`
```python
lista = ['Burbus','Gotita','Espumin']

for cat in lista:
	print(cat)

# Burbus
# Gotita
# Espumin
```

`string`
```python
kitty_babe = 'Mullen McMullen'

for char in kitty_babe:
	print(char)
# M
# u
# l
# l
# e
# n
# 
# M
# c
# M
# u
# l
# l
# e
# n
```

`tuple`
```python
tuppy = (3,5,'rosa')

  

for item in tuppy:
	print(item)

# 3
# 5
# rosa
```

`range`
```python
ran = range(0, 10, 2)

  

for number in ran:
	print(number)

# 0
# 2
# 4
# 6
# 8
```