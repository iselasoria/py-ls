## `interpolation`
String interpolation is possible through `f-strings`.  String interpoation with f-strings is one way python does [[implicit_coercion]]. In the case of the integer referenced by variable `age`, when 
The construction of an f-string is as follows:
```python
name = 'Isela'
surname = 'Soria'
age = 33

print(f'My name is {name} {surname} and I am {age}.')
```
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
print(jersey.isalnum()) # True because this string contains only numbers and alphabet characters

jersey_mod = 'Chicharito 14'
print(jersey_mod.isalnum()) # False because this string has a space
```


## `.isalpha()`
This method returns true if all the characters in the string are in the alphabet.

```python
str1 = 'onomatopeia'
cat1 = 'burbus10192020'

print(str1.isalpha()) # True
print(cat1.isalpha()) # False
```
## `.isdigit()`
Returns `True` if all the characters in the string are digits.
```python
dob = '01011991'
first_birthday = 'Jan 01 1991'


print(dob.isdigit()) # True
print(first_birthday.isdigit()) # True
```

## `.islower()`
```python
str1 = 'onomatopeia'
cat1 = 'Burbus'

print(str1.islower()) # True
print(cat1.islower()) # False
```
## `.isupper()`
This method returns `True` when all the characters in the string are uppercase letters.
```python
dob = '01011991'
first_birthday = 'Jan 01 1991'

print(dob.isdigit())
print(first_birthday.isdigit())
```
## `.join()`
Converts the contents of an iterable and returns a new string. Must use a string as the separator.

```python
clap_back = ['You','don\'t', 'own', 'cats', 'cats' ,'own','you', '!']

print((" *clap* ").join(clap_back))

# You *clap* don't *clap* own *clap* cats *clap* cats *clap* own *clap* you *clap* !
```

## `.lower()`
`.lower()` returns a new string with all the characters in lower case letters.
```python
surname = 'Soria'
print(surname.upper()) # soria
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


## `.split()`
This method uses a default argument of a blank space ` `  but can take any other separator, and returns a list containing each of the partitions made from the original string at the separator.
```python
normal_string = 'this is a normal string'
uglier_string = 'messy,string,with,lot\'s,of,commas'

print(normal_string.split())
print(uglier_string.split(','))
# ['messy', 'string', 'with', "lot's", 'of', 'commas']
```
## `.swapcase()`
This method will return a new string with the case swapped.
```python
surname = 'Soria'
print(surname.swapcase()) # sORIA
```

## `upper()`
this method will return a new string with all the characters in uppercase
```python
surname = 'Soria'
print(surname.upper()) # SORIA
```

## 