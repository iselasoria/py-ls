#fundamentals 

### Starting dataset
```python
xelas_friends = {'Jen','Ana','Esteban','Johnny','Karen'}
ryans_friends = {'Davey','Johnny','Karen','Clara','Toby'}
```
#### `.add()`
This method lets us add an element to a set. If the element is already there, it does nothing.
```python
invitations.add('Alex') 
print(invitations) # {'Ana', 'Karen', 'Esteban', 'Jen', 'Toby', 'Davey', 'Johnny', 'Alex', 'Clara'}
```

#### `.update()`
This method adds elements from a second set to the calling set. This method has the side effect of mutating the original set in place, but it returns `None`.
```python
invitations.update({'Connor', 'Greg', 'Kieran'})
print(invitations) # {'Clara', 'Connor', 'Kieran', 'Johnny', 'Jen', 'Toby', 'Davey', 'Greg', 'Esteban', 'Karen', 'Ana'}
```

#### `.remove()`
This lets us remove elements from a set, but if the element is not found, it raises a `KeyError`.
```python
invitations.remove('Alex')
print(invitations) # {'Ana', 'Clara', 'Esteban', 'Davey', 'Karen', 'Toby', 'Jen', 'Johnny'}


invitations.remove('Cindy') # raises KeyError
```

#### `.discard()`
We can use this method if we want to remove en element from the set and not raises errors if the element is not found:"

```python
invitations.discard('Cindy') # does nothing because the element is not found but it also does not raise any errors.
```


#### `.clear()`
This method clears a set entirely:
```python
invitations.clear()
print(invitations) # set()
```


#### `.union() / |` 
The union operator allows us to combine elements from two [[set]] while keeping the two initial sets untouched. 
```python
# these both do the same
invitations = xelas_friends | ryans_friends
invitations = xelas_friends.union(ryans_friends)

print(invitations) # {'Clara', 'Johnny', 'Esteban', 'Toby', 'Davey', 'Karen', 'Ana', 'Jen'}
```

#### `.intersection() / &`
The `itersection` method works like a Ven Diagram, where the return of the intersection is the middle of the diagram; that is, it returns a set of common elements between the two starting sets. 
```python
# these do exaclty the same and neither mutate either set.
mutual_friends = xelas_friends & ryans_friends
mutual_friends = xelas_friends.intersection(ryans_friends)

print(mutual_friends)
```

#### `.difference() /  -`
The `.difference()` method or `-` operator works by returning what is in one set but not in the other:
```python
only_xelas_friends = invitations - ryans_friends
only_ryans_friends = invitations - xelas_friends
print(only_xelas_friends) # {'Ana', 'Esteban', 'Jen'}
print(only_ryans_friends) # {'Toby', 'Davey', 'Clara'}
```


#### `.issubset() / <= /`
A subset is when all elements of the first set, are also present in the second set.
```python
# these two do the same
xelas_invitations = xelas_friends.issubset(invitations)
xelas_invitations = xelas_friends <= invitations

print(xelas_invitations) # True because `xelas_friends` are all on the invitation list
```
##### `<` The proper subset operator
This operator checks if the first set is a subset of the second set but they are _NOT_ equal.
```python
xelas_invitations = xelas_friends < xelas_friends
print(xelas_invitations) # False becase the sets are equal
```

#### `.issuperset() / >=`
A superset is when all elements of the second set are present in the first.
```python
ryans_invitations = invitations.issuperset(ryans_friends)
print(ryans_invitations) # True because the `invitations` set contains all of `ryans_friends`
```
##### `>` The proper superset operator.
This operator checks if the first set is a superset of the second set but they are _NOT_ equal.
```python
ryans_invitations = ryans_friends < ryans_friends
print(ryans_invitations) # False because the sets are equal
```
#### `.isdisjoint()`
This method determines if the intersection of two sets is empty-- that is, if the two sets have no values in common. 
```python
wedding_crashers = {'Caroline','Stephanie','Jeff'}
strangers = invitations.isdisjoint(wedding_crashers)

print(strangers) # True
```