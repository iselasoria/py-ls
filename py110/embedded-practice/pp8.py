"""
Given the following string, create a dictionary that represents the frequency with which each letter occurs.
The frequency count should be case sensitive.
"""

statement = "The Flintstones Rock"

ltr_frequency = {}

for ch in statement:
    ltr_frequency.setdefault(ch, 0)
    ltr_frequency[ch] += 1
print(ltr_frequency)