Lists are one of several [[collections]] in Python. A list is a [[sequences]], which means it is indexed. Lists can be mutated after creation, and can contain any object in their elements, including other lists.

```python
lst = ['Burbus', 'Gotita', 'Espumin']
```

There are several [[lists_methods]] that allow us to retrieve elements from, or mutate the list. 

Since lists are mutable objects, Python uses [[pass_by_reference]] when they are arguments to a function. This allows for any mutating methods to indeed update the list itself.
