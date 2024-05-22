## `interpolation()`

## `.capitalize()`
Capitalizes the first letter in the [[sequences]].

```python
name = 'isela'
print(name.capitalize()) # Isela
```

## `.casefold()`
Converts a [[strings]] to all lowercase.

```python
name = 'iSeLa'

print(name.casefold()) # isela
```

## `count()`
Counts the number of occurrences in the string of the argument character. Case sensitive.
```python
name = 'Burbus'

print(name.count('b')) # 1
print(name.casefold().count('b')) # 2
```

## `endswith()`
Returns a boolean of whether the string ends with the argument character or not. The argument can be a sequence of characters. Case sensitive.
```python
name = 'Burbus'

print(name.endswith('os')) # False
print(name.endswith('us')) # True
```

## `.find()`
Searches the string and returns the index of the first occurrence of the argument character. If the character is not found in the string, it returns `-1`.


```python
name = 'Gotita'
print(name.find('t')) # 2
```

## `.format()`
This used to be used before direct string interpolation became possible via f-strings. The method is called on the string literal with `{}` for placeholder and then we pass the variable names in the order of appearance in the string.

```python
name1 = 'Gotita'

name2 = 'Espumin'

  

print("{} is a very cute kitty cat! So is {}.".format(name1, name2))
# Gotita is a very cute kitty cat! So is Espumin.
```

## `.isalnum()`

This is used to check that the contents of a string are all numeric.

```python
jersey = 'Chicharito14'
print(jersey.isalnum()) # True

jersey_mod = 'Chicharito 14'
print(jersey_mod.isalnum()) # False
```


## `.isalpha()`

## `.islower()`
```python
str1 = 'onomatopeia'
cat1 = 'Burbus'

print(str1.islower())
print(cat1.islower())
```

## `.join()`
Converts the contents of an iterable and returns a new string. Must use a string as the separator.

```python
clap_back = ['You','don\'t', 'own', 'cats', 'cats' ,'own','you', '!']

print((" *clap* ").join(clap_back))

# You *clap* don't *clap* own *clap* cats *clap* cats *clap* own *clap* you *clap* !
```

## `.partition()`
This method is called on a string and takes a string as an argument. It partitions the caller into three and returns a [[`tuple`]] with the argument string being the middle element in the new tuple.
```python
str1 = 'onomatopeia'
cat1 = 'Burbus'
city1 = 'Denver'

print(str1.partition('no'))
print(cat1.partition('rb'))
print(city1.partition('e'))
```
