import pdb
import random

deck = [
    ['H','2'], ['H','3'], ['H','4'], ['H','5'], ['H','6'], ['H','7'], ['H','8'], ['H','9'], ['H','10'], ['H','J'], ['H','Q'], ['H','K'], ['H','A'],
    ['D','2'], ['D','3'], ['D','4'], ['D','5'], ['D','6'], ['D','7'], ['D','8'], ['D','9'], ['D','10'], ['D','J'], ['D','Q'], ['D','K'], ['D','A'],
    ['C','2'], ['C','3'], ['C','4'], ['C','5'], ['C','6'], ['C','7'], ['C','8'], ['C','9'], ['C','10'], ['C','J'], ['C','Q'], ['C','K'], ['C','A'],
    ['S','2'], ['S','3'], ['S','4'], ['S','5'], ['S','6'], ['S','7'], ['S','8'], ['S','9'], ['S','10'], ['S','J'], ['S','Q'], ['S','K'], ['S','A']
]

# set up hands and scores
player_hand = []
dealer_hand = []
scores = {'player': [], 'dealer': []}


def prompt(msg):
    print(f"==> {msg}")

def shuffle(deck):
    # shuffle the deck
    random.shuffle(deck)


def evaluate_face_value(card):
    face = card
    match face:
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case 'J' | 'Q' | 'K':
            return 10
        case 'A':
            calculate_ace_value(hand)





def tally_up_score(hand): # take the sum of the cards in the hand
    tally = []
    for card in hand:
        tally.append(evaluate_face_value(card[1]))
    return sum(tally)

def update_scoreboard(participant, hand):
    scores[participant] = tally_up_score(hand)



def display_card(suit_card): # display current card selected from the deck at random needs work
    match suit_card[0]:
        case 'H':
            print("+-----+")
            print(f"|{suit_card[1]}    |")
            print(f"|  {chr(9829)}  |")
            print(F"|    {suit_card[1]}|")
            print("+-----+")
        case 'D':
            print("+-----+")
            print(f"|{suit_card[1]}    |")
            print(f"|  {chr(9830)}  |")
            print(F"|    {suit_card[1]}|")
            print("+-----+")
        case 'S':
            print("+-----+")
            print(f"|{suit_card[1]}    |")
            print(f"|  {chr(9824)}  |")
            print(F"|    {suit_card[1]}|")
            print("+-----+")
        case 'C':
            print("+-----+")
            print(f"|{suit_card[1]}|    ")
            print(f"|  {chr(9827)}  |")
            print(f"|    {suit_card[1]}|")
            print("+-----+")




def display_score(hand): # display the current score
    prompt(f"Your're at {hand[1]}.")

def hit(deck): # suffle, choose and remove from deck. Display the chosen card and current score
    shuffle(deck)
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_ace_value(ace_card):
    pass


def busted(hand):
    tally_up_score(hand) >= 21

def deal_kickoff(deck): # distribute two cards to players and set up scores
    shuffle(deck)
    print(player_hand)
    for _ in range(1,3):
        tmp_card = deck.pop()
        player_hand.insert(1, tmp_card)
        display_card(tmp_card)

    # [deck.pop(), deck.pop()] # [hit(deck) for _ in range(1,3)]
    dealer_hand = [deck.pop(), deck.pop()]
    print(f"_________{display_card(player_hand)}")
    # print(f"Player, you have the following cards: {player_hand} and your tally is at {tally_up_score(player_hand)}.")
    # print(f"The Dealer has {dealer_hand[-1]} and a mystery card. Tread wiseley.")




deal_kickoff(deck)
# tally_up_score(player_hand)

print(f"PLAYER HAND IS: {player_hand}")

while True:
    # game logic
    prompt('Do you want to stay or hit?')
    answer = input()

    if answer == 'stay':# or busted():
        break
    elif answer == 'hit':
        print(player_hand)
        player_hand.append(hit(deck))
        print(player_hand)

    break

