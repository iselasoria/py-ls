"""What would the output of the code below be?"""

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# Solution
# This would raise an AttributeError because frozensets are immutable objects.