# Functions
Date: 08-02-2024

| Left columns  | Right columns |
| :-----------: |:-------------:|
| Date          | 08-02-2024    |
| Atendees      | Baur, Lionel, Rosie |
| left baz      | right baz     |

---
---

Overview:

    - Functions vs. Methods
    - Built-in Functions
    - Scope
    - Arguments and Parameters
    - Return Values
    - Side Effects*

If time allows:

    - iteration
    - nested iteration

## Built-in Functions
Functions that are always available in the interpreter and you don't need to import any packages to access them.
```python
  print()
  input()
  len()
  zip()
  id()
```

---

## Scope
Python's rules of scope:

    L-ocal
    E-nclosing
    G-lobal
    B-uilt-in

1. What happens when you run the following snippet?
    ```python
    def well_howdy(who):
        greeting = 'Howdy'
        print(f'{greeting}, {who}')

        well_howdy('Angie')
        print(greeting)
    ```

2. What happens when you run the following snippet?
    ```python
    im_outside = 'Hi, from the outside!'

    def my_fxn():
        mystery_param = 'Who am I?'
        print(im_outside)

    my_fxn()
    print(mystery_param)
    ```

---

## Arguments and Paramters
`Paramters` are the names used in defining what the function will take as input, `arguments` are the data we pass in at the time of invocation.

```python
def my_fxn(i_am_param):
  print(i_am_param)

i_am_arg = 'I\'ve been passed to the function'
my_fxn(i_am_arg)
```
#### Default parameters
```python
def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!
```

---

## Return Values
The `return` statement is used inside a function to stop execution and _return_ the result back to the caller. By default, the return of a function in Python is `None`.

```python
def add(a, b):
    return a + b

add(2, 3)           # returns 5
```

Return based on condition:
```python
def is_digit(char):
    if char >= '0' and char <= '9':
        return True

    return False
```

---
## Review of Iteration:
#### `While` Loops

```python
counter = 0

while counter >= 10:
    print(counter)
    counter += 1
```

When you want to execute the code at least once, for example, when you kick off a game, and then you ask if they want to play again:

```python
counter = 0

while counter <= 0:
    counter += 1
    print(counter)
```
#### `for` Loops

For loops allow us to iterate through a collection, they don't rely on a counter and they have a pre-defined stop-- the end of the collection.

```python
name = 'Joe'
for ch in name:
    print(ch)
```

#### Nested `for` Loops
Nested for loops have two or maybe more levels of iteration, although having more than two is not adviced.

```python
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace',
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f'{rank} of {suit}'
        deck.append(card)

print(deck)
```
