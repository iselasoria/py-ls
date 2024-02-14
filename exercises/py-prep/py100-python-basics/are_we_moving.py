# determine what this prints:


speed = 0
acceleration = 24
braking_force = 19

is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
                # 19 < 24 and (False or True)
                # 19 < 24 and True
                # True and True
                # True
print(is_moving)

# BONUS: did we need the parenthesis or coudl we have the folllowing:

# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0

# yes, we need the parentheses because `and` has a higher operator presedence than `or`
