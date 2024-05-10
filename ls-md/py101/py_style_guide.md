# Naming conventions

Python follows a set of style guideliness, some of which are necessary.
Naming conventions for identifiers, including constants and class names:
- use `snake_case`
- names can contain underscores, lowercase letters, and numbers `0-9`
- names must begin with a letter
- if the name has multiple words, separate with a `_`
- names that begin/end with `__` have special meaning, so don't use them until you understand
- names can only use letters and digits from ASCII.


|                   | Idiomatic           | Non-Idiomatic                                | Illegal                        |
| ------------------|-------------------- |:--------------------------------------------:| -------------------------------|
| **[[variables]]** | `snake_case`/ `idx1`| `snakecase` / `Snake_case` / `_snake case `  | `snake case` / `12snake_case`  |
| **classes**       | `FourLeggedPets`    |   `fourWayIntersection`                      | `pass`/ `3xy`/ `is_lowercase?` |
| **[[constants]]** | `WINNING_SCORE`     | Python constant naming conventions are advisory only.

Indentation matters and it should be used as 4 spaces, not tabs.