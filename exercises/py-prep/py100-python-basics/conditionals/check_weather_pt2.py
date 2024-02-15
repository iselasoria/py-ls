

# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.
"""
It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather."""

weather = 'rainy'

match weather:
  case 'sunny':
    print("It's a beautiful day!")
  case 'rainy':
    print('Grab your umbrella!')
  case _:
      "Let's stay inside"