import random

VALID_CHOICES = ['rock','paper','scissors','lizard','spock']

WINNING_MOVES = {
    'rock': ['scissors','lizard'],
    'paper': ['rock','spock'],
    'scissors': ['lizard','paper'],
    'lizard': ['paper','spock'],
    'spock' : ['scissors','rock']
}

def prompt(msg):
    print(f'==> {msg}')

def win(first, second):
    if second in WINNING_MOVES[first]:
        print(WINNING_MOVES[first])
        return True

    # if the first score is included as a key, and the second is included as a value
    # this returns true for a win

def display_winner(score1, score2):
    if win(score1, score2):
        print('The player wins this round!')
    elif win(score2, score1):
        print('The computer wins this round!')
    else:
        print('We have a tie!')
    # if when we pass player as the first arg to _win_ we get true
        # then display the player won
    # otherwise if the pass the scores swapped
        # return that the computer on
    # otherwise, return that it is a tie

# def display_winner(player, computer):
#     if ((player == 'rock' and computer == 'scissors') or
#         (player == 'paper' and computer == 'rock') or
#         (player == 'scissors' and computer == 'paper')):
#         prompt('You win!')
#     elif ((player == 'rock' and computer == 'paper') or
#           (player == 'paper' and computer == 'scissors') or
#           (player == 'scissors' and computer == 'rock')):
#         prompt('Computer wins!')
#     else:
#         prompt('It\'s a tie!')


while True:

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')

    choice = input()


    while choice not in VALID_CHOICES:
        prompt('That\'s not a valid choice')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose: {choice}, the computer chose: {computer_choice}')

    display_winner(choice, computer_choice)

    # break if the user doesnt want to play
    prompt('Do you want to play again (y/n)?')
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0]=='n':
        break
