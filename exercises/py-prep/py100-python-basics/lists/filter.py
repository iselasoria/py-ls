# Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]

over_100 = 0

for num in scores:
    if num >= 100:
        over_100 += 1

print(over_100)