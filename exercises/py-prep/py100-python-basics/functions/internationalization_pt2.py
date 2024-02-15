# Building on your solutions from the previous exercises, write a function local_greet that 
# takes a locale as input, and returns a greeting. The locale lets us greet people from 
# different countries appropriately, even when they share a common language, for example:
def extract_language(locale):
  return locale[:2]

def extract_region(locale):
  return locale[3:5]

def local_greet(locale):
  lang = extract_language(locale)
  reg = extract_region(locale)
  
  if lang == 'en':
    if reg == 'UK':
      return 'Oi mate!'
    elif reg == 'US':
      return 'What\'s up!'
  elif lang == 'fr':
    if reg == 'CA':
      return 'Salut! Je suis canadienne!'
    elif reg == 'FR':
      return 'Moi, je suis francaise!'


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia 
# in your implementation, and feel free to fall back on the language-specific greetings 
# in all other cases, for example:


print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
# print(local_greet('fr_MA.UTF-8'))       # Salut!

# When implementing local_greet, make sure you re-use your extract_language, 
# extract_region, and greet functions from the previous exercises.