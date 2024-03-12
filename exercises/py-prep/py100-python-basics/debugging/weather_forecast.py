"""
Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. However, 
the output is the same every time the function is invoked. Why? Fix the code so that it behaves as expected.
"""

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

# the bug exists because sunshine will always be a string object, rather than a boolean. In Python, non-empty strings
# are always truthy so this code will always execute the first option in the if statement