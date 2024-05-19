Ranges are date types that hold numeric ranges.
You can't have range literals, instead you always need to declare them with the constructor `range()`.

The `range()` constructor takes a required argument that becomes the high end of the range. By default, ranges start at 0.

```python
range(high_end_of_range)

r = range(10) # range(0, 20)
```

From here, we can access the elements in the range via index:

```python
r = range(10)
print(r[0]) # 0
print(r[3]) # 3
```

We can also pass a second argument-- the low end of the range:

```python
range(low_end_of_range, high_end_of_range)

r = range(4, 10)
print(r[0]) # 4
print(r[3]) # 7
```

We can go one step further and add a third argument-- the step:

```python
range(low_end_of_range, high_end_of_range, step)
r = range(0, 101, 5)
print(r[0]) # 0
print(r[1]) # 5
print(r[2]) # 10
```

The step is a useful tool that allows us to reverse. If we use this, we must swap the first two arguments so that it now reads:

```python
range(high_end_of_range, low_end_of_range, step)
r = range(100, 1, -2)
print(r[0]) # 100
print(r[1]) # 98
print(r[2]) # 96
```

