# in the previous problem you added 'Dino' to the list like this:

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")

# how can we add multiple items to the list, like 'Dino' and 'Hoppy'?
# Replace the calle to append with another method invocation

flintstones += ['Dino','Hoppy']

print(flintstones)

# LS Solution:
flintstones.extend(['Dino','Hoppy'])
# ! what are the technical differences between extend and mutating the list like above