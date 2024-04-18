import random

VALID_CHOICES = ['rock','paper','scissors','lizard','spock']

WINNING_MOVES = {
    'rock': ['scissors','lizard'],
    'paper': ['rock','spock'],
    'scissors': ['lizard','paper'],
    'lizard': ['paper','spock'],
    'spock' : ['scissors','rock']
}

# score tracking
user_score = []
comp_score = []
WINNING_SCORE = 3

def prompt(msg):
    """Prompting mesage"""
    print(f'==> {msg}')

def win(first, second):
    """Determining the winner of a round"""
    if second in WINNING_MOVES[first]:
        return True

def display_winner(score1, score2):
    """Displaying the winner of the round"""
    if win(score1, score2):
        print('The player wins this round!')
    elif win(score2, score1):
        print('The computer wins this round!')
    else:
        print('We have a tie!')

def valid(choice):
    """Determining if the choice is valid"""
    if choice[0] in [option[0] for option in VALID_CHOICES]:
        return True
    return False

def shorthand_convert(choice):
    """Converting shorthand input into full word"""
    # ! minor bug when someone just enters 's'
    match choice:
        case 'r' | 'rock':
            return 'rock'
        case 'p' | 'paper':
            return 'paper'
        case 'l' | 'lizard':
            return 'lizard'
        case 'sp' | 'spock':
            return 'spock'
        case 'sc' | 'spock':
            return 'scissors'

def game_tally(first, second):
    """Used to tally scores, no returns, no displays, just side effects"""
    if second in WINNING_MOVES[first]:
        user_score.append('win')
    elif first in WINNING_MOVES[second]:
        comp_score.append('win')





while True:

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')

    choice = shorthand_convert(input())


    while not valid(choice):
        prompt('That\'s not a valid choice')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose: {choice}, the computer chose: {computer_choice}')

    game_tally(choice, computer_choice)

    display_winner(choice, computer_choice)

    # break if the user doesnt want to play
    prompt('Do you want to play again (y/n)?')

    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if len(user_score) == WINNING_SCORE:
        print('You won this match!')
        break
    elif len(comp_score) == WINNING_SCORE:
        print('The computer wins the match!')
        break
# !minor bug when someone wins, come back to this.
    if answer[0]=='n':
        break
