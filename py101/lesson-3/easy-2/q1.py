# write two distinct ways of reversibng the list wihtout mutatin the original

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# rev = [numbers[-1] for num in numbers]

# solution 1:
rev = numbers[::-1] #using the ranges #! return to this slicing

# solution 2:
rev = list(reversed(numbers))
# print(rev)

# solution 3:
reversed_manual = []
for idx in range(1, len(numbers)):
    reversed_manual.append(numbers[-idx])

reversed_manual.append(numbers[0])

print(reversed_manual)