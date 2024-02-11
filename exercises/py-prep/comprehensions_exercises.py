# 1
# The following code causes an infinite loop (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# the reason this is an infinite loop is we never update `counter` and therefore, the condition is always true; 0 will always be less than 5.
    
# 2
    
# Modify the age.py program you wrote in Exercise 6 of the Variables chapter.
# The updated code should use a for loop to display the future ages.
    
"""
age = 22
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')
"""


age = int(input('What is yur age? '))
print(f'Today, you are {age} years old.')

for edad in range(10, 51, 10):
    print(f'In {edad} years, you will be {age + edad} years old.')