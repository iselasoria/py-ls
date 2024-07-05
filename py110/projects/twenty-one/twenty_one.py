import random

deck = [
    ['H','2'], ['H','3'], ['H','4'], ['H','5'], ['H','6'], ['H','7'], ['H','8'], ['H','9'], ['H','10'], ['H','J'], ['H','Q'], ['H','K'], ['H','A'],
    ['D','2'], ['D','3'], ['D','4'], ['D','5'], ['D','6'], ['D','7'], ['D','8'], ['D','9'], ['D','10'], ['D','J'], ['D','Q'], ['D','K'], ['D','A'],
    ['C','2'], ['C','3'], ['C','4'], ['C','5'], ['C','6'], ['C','7'], ['C','8'], ['C','9'], ['C','10'], ['C','J'], ['C','Q'], ['C','K'], ['C','A'],
    ['S','2'], ['S','3'], ['S','4'], ['S','5'], ['S','6'], ['S','7'], ['S','8'], ['S','9'], ['S','10'], ['S','J'], ['S','Q'], ['S','K'], ['S','A']
]
print(len(deck))

def prompt(msg):
    print(f"{msg}")

def shuffle(deck):
    random.shuffle(deck)

def tally_up_score(hand):
    pass
    # take the sum of the cards in the hand
def display_card(hand):
    prompt(f"The card you got is: {hand}")

def display_score(hand):
    prompt(f"Your're at {hand[1]}.")

def hit(deck):
    shuffle(deck)
    card = random.choice(deck)
    deck.remove(card)
    display_card(card)
    display_score(card)
    return card

def calculate_ace_value(ace_card):
    pass


def busted(hand):
    tally_up_score(hand) >= 21

# set up hands and scores
player_hand = []
dealer_hand = []
scores = {'player': 0, 'computer': 0}

# distribute cards to players
print(len(deck))
player_hand = hit(deck)
print(len(deck))

while True:
    # game logic
    prompt('Do you want to stay or hit?')
    answer = input()

    if answer == 'stay':# or busted():
        break
    elif answer == 'hit':
       player_hand.append(hit(deck))
       print(player_hand)

    break

