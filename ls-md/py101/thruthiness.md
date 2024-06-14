#fundamentals 
The concept of truthiness in programming refers to whether a value would resolve as thruthy, not necessarily `True`.
For example, in Python, there are values that evaluate as _falsey_:


| _Truthy_                                            | _Falsey_ |
| --------------------------------------------------- | :------: |
| `'I have a value, so I'm truthy'`                   |   `''`   |
| `['Hi', 'I\'m', 'truthy']` \| [`None`]              |   `[]`   |
| `(2,6,12)`                                          |   `()`   |
| `{'thruiness' : 'Don\'t look at me, I\'m truthy!'}` |   `{}`   |
|                                                     |  `None`  |
|                                                     |   `0`    |
|                                                     |  `0.0`   |
