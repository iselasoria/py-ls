# You want to add the numbers from 1 to 5 to a list, but the code 
# below is not producing the expected result. How can you fix it?

numbers = []

for i in range(5): # range(1,6)
    numbers.append(i)

print(numbers)

# range is exclusive of the last item on the range, so in this case to get 1-5 we need to use 6 as the upperbound range
# and use 1 as the bottom of the range because range is inclusive of the bottom range
