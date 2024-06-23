# PEDAC PRCTICE
---

## Problem
Rules:
- building blocks are cubes
- structure has layers
- top layer will be a single block
- a block in an upper layer must be supported by four blocks in a lower layer
- a block in a lower layer can support more than one block in an upper layer
- there must be no gaps

I: integer --> the number of available blocks
O: integer --> the number of leftover blocks after building the tallest possible structure

Q:
- what makes a structure valid vs. invalid?
    - is a layer valid if it were to have more blocks than 4 supporting each top block
- is it implied that we'll always have leftover blocks?

Implicit Rules:
- since bottom blocks can support several top blocks, there is overlapping
    - a top block can have support from more than 1 bottom block
- layer number correlates with blocks in layer
- the number of blocks in a layer is layer number * layer number

## Test Cases
```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

**Revised Rules Based on Test Cases**
- A structure will not always have leftover blocks
- A structure that is given no available blocks will have none leftover
- A structure that is given less than 5 blocks to start with will only have one layer and the rest of the blocks remain
- A top block must be supported by exactly 4 bottom blocks, no more no less

## DS:
- we need a structure that we can nest
- the data structure needs to be mutable so we can change it as we go though its construction
- Potentially a list

## Model Solution:
[]
[][][][]
[][][][][][][][][]

## Algo:
- initialize `blocks_remaining` to `available_blocks` argument

- For each layer number starting with 1 (this is the topmost layer)
- check valid layer:
    - a valid layer contains previous layer's blocks * 4
- Square the layer number and subtract from the `available_blocks`
- return the `blocks_remaining`


