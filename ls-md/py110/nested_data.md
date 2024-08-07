#fundamentals 
## Nested Data Structures 
Nested data structures are data structures that contains other data structures within them.
```python
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nested_dict = {
    'a': {'x': 1, 'y': 2},
    'b': {'x': 3, 'y': 4},
    'c': {'x': 5, 'y': 6}
}

dict_of_lists = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'broccoli', 'spinach']
}
```


## Nested Iteration
Nested iteration involves iterating at two levels or more to access specific values. 

```python
shopping_haul = [
	{'groceries': ['milk','coffee','cereal']},
	{'cleaning_supplies': ['fabuloso','bleach','dish soap']},
	{'toiletries':['toothpaste','deodorant','hand cream']},
]
# find the hand cream in the shopping haul

for bag in shopping_haul: 
	for items in bag.values(): 
		if 'hand cream' in items: 
			print("Found the hand cream")
```





Bonus sorting practice!

How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent? 
```python
books = [
	{
		'title': 'One Hundred Years of Solitude',
		'author': 'Gabriel Garcia Marquez',
		'published': '1967',
	},
	
	{
		'title': 'The Book of Kells',
		'author': 'Multiple Authors',
		'published': '800',
	},
	
	{
		'title': 'War and Peace',
		'author': 'Leo Tolstoy',
		'published': '1869',
	},

]
```

```python
def pub_yr(book):
	return int(book['published'])

  

sorted_books = sorted(books, key=pub_yr)
print(sorted_books) # [{'title': 'The Book of Kells', 'author': 'Multiple Authors', 'published': '800'}, {'title': 'War and Peace', 'author': 'Leo Tolstoy', 'published': '1869'}, {'title': 'One Hundred Years of Solitude', 'author': 'Gabriel Garcia Marquez', 'published': '1967'}]
```