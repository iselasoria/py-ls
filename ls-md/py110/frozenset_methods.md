### Dataset to be used:
```python
ls_cats = frozenset(["Beemo","Quica","Cheddar","Beemo","Pudding","Cocoa","Burbus","Gotita","Espumin"])

xelas_cats = frozenset(["Burbus","Gotita","Espumin","Clovis","Molonchita"])
```

#### `.union() | /`
`.union()` combines two [[frozenset]] into a new object of the same type. These both do the same:

```python
all_cats = ls_cats.union(xelas_cats)
all_cats = ls_cats | xelas_cats
print(all_cats) # frozenset({'Beemo', 'Espumin', 'Quica', 'Pudding', 'Cocoa', 'Burbus', 'Cheddar', 'Gotita'})
```

#### `.intersection()`
The `.intersection()` method returns a new object of the `frozenset` type. 
```python
gratuitous_cats = ls_cats.intersection(xelas_cats)
print(gratuitous_cats) # frozenset({'Gotita', 'Burbus'})
```

#### `.difference()`
The `.difference()` method returns a new object of the `frozenset` type containing all elements that are in the calling `frozenset`, but _NOT_  in the `frozenset` that got passed in as the argument.


```python
only_ls_cats = all_cats.difference(xelas_cats)
print(only_ls_cats) # frozenset({'Cocoa', 'Quica', 'Beemo', 'Pudding', 'Cheddar'})
```

#### `.issubset()`
This method returns `True` if all the elements from the calling `frozenset` are found in the argument `frozenset` and `False` otherwise
```python
print(xelas_cats.issubset(all_cats)) # True
print(all_cats.issubset(xelas_cats)) # False
```

#### `.issuperset()`
This method is complementary to the `.issubset()` method. `.issuperset()` checks if all the elements on the argument `frozenset` are present in the calling `frozenset`. 

```python
print(f"Xelas cats are a subset of All Cats: {xelas_cats.issubset(all_cats)}")

print(f"All Cats are a superset of Xela's cats: {all_cats.issuperset(xelas_cats)}")

# Xelas cats are a subset of All Cats: True
# All Cats are a superset of Xela's cats: True
```

> If `A.issubset(B)` returns `True`, it means that all elements of `A` are in `B`, so `B.issuperset(A)` should also return `True`. Conversely, if `A.issuperset(B)` returns `True`, it means that all elements of `B` are in `A`, so `B.issubset(A)` should also return `True`.

#### `.isdisjoint()`
This method returns `True` if two `frozensets` have no elements in common. 
```python
instagram_cats = frozenset(['Siberian Simon','Moe Grey','Zelda','Fiddy','Primus', 'Bubby'])

print(xelas_cats.isdisjoint(instagram_cats)) # True because there are no elements in common
```