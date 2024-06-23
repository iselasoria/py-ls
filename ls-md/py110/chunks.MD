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