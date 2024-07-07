import os
import pdb
import time
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
    print(f"Shuffling the deck")
    time.sleep(2)
    print(f"\033[32;5m{chr(9829)}\033[0m")
    time.sleep(.5)
    print(f"\033[32;5m{chr(9830)}\033[0m")
    time.sleep(.5)
    print(f"\033[32;5m{chr(9824)}\033[0m")
    time.sleep(.5)
    print(f"\033[32;5m{chr(9827)}\033[0m")
    time.sleep(2)
    os.system('clear')
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
        case '10' | 'J' | 'Q' | 'K':
            return 10
        case 'A':
            return 100
            # return 100 #calculate_ace_value(player_hand)


def tally_up_score(hand): # take the sum of the cards in the hand
    tally = []
    for card in hand:
        tally.append(evaluate_face_value(card[1]))
    # pdb.set_trace()
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
    # pdb.set_trace()
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_ace_value(hand):
    if tally_up_score(hand) >= 21:
        return 1
    else:
        return 11
    # print()
    # print(hand)

    # hand_val = [num for num in hand[1][1] for num in hand]
    # print()
    # print(f"Hand value to calc ace: {hand_val}")

def busted(hand):
    # print(f"HAND: {hand}")
    return bool(tally_up_score(hand) >= 21)

def dealer_turn(deck):
    print('Dealer turn.........')
    time.sleep(3)
    while scores['dealer'] <= 17:
        dealer_temp = hit(deck)
        print('The dealer just drew:')
        display_card(dealer_temp)
        dealer_hand.append(dealer_temp)
        scores['dealer'] = tally_up_score(dealer_hand)
        print(scores)
        if busted(dealer_hand):
            print("Dealer just busted, player wins!")
        break

def deal_kickoff(deck): # distribute two cards to players and set up scores
    shuffle(deck)

    print("Your cards are: ")
    for _ in range(1,3):
        tmp_card = deck.pop()
        player_hand.insert(1, tmp_card)
        display_card(tmp_card)


    print('The Dealer has the following plus one mystery card:')

    for _ in range(1,3):
        dtpm_card = deck.pop()
        dealer_hand.insert(1, dtpm_card)
    display_card(dtpm_card)

    update_scoreboard('player', player_hand)
    update_scoreboard('dealer', dealer_hand)
    print(f"SCOREBOARD: {scores}")

    print(f"Player, your tally is at {scores['player']}.")
    # print(f"The Dealer has {dealer_hand} and a mystery card. Tread wiseley.")




deal_kickoff(deck)


while True:
    # game logic
    prompt('Do you want to stay or hit?')
    answer = input()

    # print(busted(player_hand))
    if busted(player_hand):
        print("YOU BUSTED at the first try, the game is over!")
        break
    elif answer == 'stay':
        print('You chose to stay, yielding the turn to the Dealer')
        break
        # loop player logic where the keeps hitting as long as his score is under 17
        # once Dealer gets close to 17, we compare both scores--> the maximum of the dictionary of scores
    elif answer == 'hit':
        player_temp_card = hit(deck)
        player_hand.append(player_temp_card)
        print('You just drew:')
        display_card(player_temp_card)
        print(player_hand)
        update_scoreboard('player', player_hand)
        print(scores)
        # pdb.set_trace()
        if busted(player_hand):
            print("YOU BUSTED AFTER YOU HIT, DEALER WINS")
            break
            # place dealer logi here
        print(f"So far::::::::{tally_up_score(player_hand)}")
        busted(player_hand)

    # dealer turn
if (busted(dealer_hand) == False) and (busted(player_hand) == False):
    dealer_turn(deck)

