"""
The following function unnecessarily uses two return statements
to return boolean values. Can you rewrite this function so
it only has one return statement and does not
explicitly use either True or False?"""

def is_color_valid(color):
    return color == "blue" or color == "green"

    # if color == "blue" or color == "green":
    #     return True
    # else:
    #     return False

# second solution
def is_color_valid(color):
    return color in ["blue", "green"] # checking if the color is in a list of approved colors