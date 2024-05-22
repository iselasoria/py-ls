```python
def change(string):
    new_str = ''
    print(f'Object ID when empty: {id(new_str)}')
    for char in string:
        new_str += char
        print(f'Object ID after populated: {id(new_str)}.')
        return new_str
change('Burbus')
```
