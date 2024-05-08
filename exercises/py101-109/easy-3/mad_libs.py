"""
Madlibs is a simple game where you create a story template with "blanks"
for words. You, or another player, then construct a list of words and
place them into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb,
and an adjective, and injects them into a story that you create.

ex:
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
"""

print('Enter a noun: ')
noun = input()

print('Enter a verb: ')
verb = input()

print('Enter a adjective: ')
adjective = input()

print('Enter a adverb: ')
adverb = input()

print(f'Many years later, as he faced the {noun}, Colonel Aureliano Buendia was to {adverb} {verb} the {adjective}  afternoon when his father took him to discover ice.')