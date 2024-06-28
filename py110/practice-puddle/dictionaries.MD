# Dictionaries

## Iterating Over Dictionaries
```python
dates = { 'first_date':
            {
                'name' : 'The Last Bookstore',
                'address': '453 S Spring St Ground Floor, Los Angeles, CA 90013',
                'cost': 0,
                'phone_number': '+12134880599'
            },
            'second_date':
            {
                'name': 'Perch',
                'address': '448 S Hill St, Los Angeles, CA 90013',
                'cost': 100,
                'phone_number': '+12138021770'
            }
}

for date in dates.values():
    for d in date:
        print(d)
```

## `.get()`
will return `None` if there argument is not found. This method searches the keys.
```python
print(dates.get('seond_date'))
# {'name': 'Perch', 'address': '448 S Hill St, Los Angeles, CA 90013', 'cost': 100, 'phone_number': '+12138021770'}
```

It can take another optional argument to return instead of `None` when the key isn't found:
```python
print(dates.get('sedond_date', 'Wait a minute, we never went there! You must have been there with your other girlfriend!'))
# Wait a minute, we never went there! You must have been there with your other girlfriend!
```

# `.in()`
Checks if the _key_ is in the dict_keys

```python
print('fourth_date' in dates) # False
print('first_date' in dates) # True

```

