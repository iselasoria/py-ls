#fundamentals 
  
The `enumerate` function allows you to access the element at the iteration, as well as its index. 
```python
books = ["One Hundred Years of Solitude","1984","Brave New World"]


for idx, book in enumerate(books):
	print(f"'{book}' is at position {idx}")
 
# 'One Hundred Years of Solitude' is at position 0
# '1984' is at position 1
# 'Brave New World' is at position 2
```