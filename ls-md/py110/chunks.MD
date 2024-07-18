# Chunks of Useful Code

## Generating Substrings
```python
word = 'madam'


def gen_subs(s):
    subs = []
    for start_idx in range(len(s)): # all thru the end of the string
        for end_idx in range(start_idx, len(s)): # starting at the moving top level iteration index and up thru the lenght of the string
            current_sub = s[start_idx:end_idx+1] # slice the string from start to end + 1
            subs.append(current_sub) # append to list
    return subs # return list

print(gen_subs('madam'))



print(gen_subs(word))
# ['m', 'ma', 'mad', 'mada', 'madam', 'a', 'ad', 'ada', 'adam', 'd', 'da', 'dam', 'a', 'am', 'm']
```

## Generating Substrings that are only vowels
```python
word = 'onomatopeia'

def gen_vowel_subs(string):
    substrings = []

    for start_idx in range(len(string)):
        for end_idx in range(start_idx,len(string)):
            sub = string[start_idx:end_idx+1]
            if all(char in 'AEIOUaeiou' for char in sub):
                substrings.append(sub)
    return substrings

print(gen_vowel_subs(word))
# ['o', 'o', 'a', 'o', 'e', 'ei', 'eia', 'i', 'ia', 'a']

```

## Generate increasing substrings
```python
def gen_subs(str):
    substrings = []
    for sliding_idx in range(len(str)):
        suby = str[:sliding_idx + 1]
        substrings.append(suby)

    return substrings
```

## Counting occurrences of a letter
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