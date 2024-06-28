# Chunks of Useful Code

## Counting occurences of a letter
```python
statement = "The Flintstones Rock"

ltr_frequency = {}

for ch in statement:
    ltr_frequency.setdefault(ch, 0)
    ltr_frequency[ch] += 1
print(ltr_frequency)
```

## Generating a list of letters a-z
```python
alpha_ords = list(range(97, 123))

def charify(num):
    return chr(num)

alphabet = map(charify, alpha_ords)
alphabet = list(alphabet)
# print(alphabet)

alpha_range = list(range(1,27))
# print(alpha_range)

alpha_positions = zip(alphabet, alpha_range)
alpha_positions = dict(alpha_positions)
print(alpha_positions)
```