A `frozenset` is a data type similar to a set, but it is immutable.
The rules of [[set]] apply, except now _immutable_.

```python
ls_cats = ["Beemo","Quica","Cheddar","Beemo"]
frozen_cats = frozenset(ls_cats)
print(frozen_cats) # frozenset({'Beemo', 'Cheddar', 'Quica'})
print(type(frozen_cats)) # frozenset
```

