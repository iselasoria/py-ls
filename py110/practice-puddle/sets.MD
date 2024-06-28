# Sets
Only hold hashable objects
Objects can only be stored once-- all unique values!
Think of sets as mini dictionaries, but without the values.

```python
setty = {3,5,1,0,0}
print(setty) # {0, 1, 3, 5}
```


## `.add()`
- Sets are mutable so we can add elements.
- All elements must be hashable

```python
cat_setty = {'Clovis','Molonchita'}
cat_setty.add('Bootsie Collins')
print(cat_setty) # {'Molonchita', 'Clovis', 'Bootsie Collins'}

Elements are hashable
cat_setty = {'Clovis','Molonchita'}
cat_setty.add('Bootsie Collins')
cat_setty.add(['not', 'a','cat']) # This will raise a Type error because all elements must be hashable.


## `.remove()`
Will remove an element from the set, but it will raise an error if the argument is not found in the set.

## `.discard()`
This is a better option to remove an elements without causing the cide to break.

# Frozen Sets
Immutable

## `.clear()`
