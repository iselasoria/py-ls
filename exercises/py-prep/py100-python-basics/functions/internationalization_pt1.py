# Use Python's control structures to create a function that takes an ISO 639-1 language code
# and returns a greeting in that language. You can take the examples below or add whatever languages you like.
def greet(lang_code):
  match lang_code:
    case 'en':
      return 'Hello!'
    case 'fr':
      return 'Salut!'
    case 'pt':
      return 'Òla!'
    case 'ar':
      return 'Mahraban!'

print(greet('ar'))
print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!