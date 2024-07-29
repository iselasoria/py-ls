# Functions
Date: 08-02-2024

| Left columns  | Right columns |
| :-----------: |:-------------:|
| Date          | 08-02-2024    |
| Atendees      | Baur, Lionel  |
| left baz      | right baz     |

---
---

Overview:

    - Functions vs. Methods*
    - Built-in Functions
    - Scope
    - Arguments and Parameters
    - Return Values
    - Side Effects*

## Scope
Python's rules of scope:

    L-ocal
    E-nclosing
    G-lobal
    B-uilt-in

1. What happens when you run the following snippet?
    ```python
    def my_fxn():
        mystery_param = 'Who am I?'

    my_fnx()
    print(mystery_param)
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