# determine what will be printed:

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}") # 3.99 will be printed. Sale is set to True on the first line
# so when we get to the second line in the ternary operator, and since the ternary operator uses
# negation to say `not sale` meaning if sale is falsey, the second expression is returned.