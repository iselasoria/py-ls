#fundamentals
variables are types of [[identifiers]] that are used to store a value. Variables don't actually hold any data themselves, but instead they point to the place in memory where the data is stored


## initialization
initialization (also called assignment) of a variable occurs simply when we give them a value through the assignment [[statement]].
```python
name = 'Rosa Isela'
```

Of the above code, it can be said that

>The variable `name` is assigned the string `Rosa Isela`


## reassignment
reassignment refers to the action of removing the connection from one variable to data stored in memory and connecting another different datum.

```python
greeting = 'Hello'
```

Here, the string 'Hello' gets stores somewhere in memory, let's pretend it's stored at id location ID: 450. The `greeting` variable also gets stored in a place in memory, say ID: 300. Now we would have a connection between the two. Later, when we want to reassign, the connection between those two would break and a new one would form between the id of the identifier and that of the new string it will point to from now on.

![[reassignment-visual.png]]

