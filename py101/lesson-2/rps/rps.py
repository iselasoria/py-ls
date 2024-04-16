import random

VALID_CHOICES = ['rock','paper','scissors']

def prompt(msg):
    print(f'==> {msg}')

prompt(f'Choose one: {", ".join(VALID_CHOICES)}')

choice = input()


while choice not in VALID_CHOICES:
    prompt('That\'s not a valid choice')
    choice = input()

computer_choice = random.choice(VALID_CHOICES)

prompt(f'You chose: {choice}, the computer chose: {computer_choice}')

if ((choice == 'rock' and computer_choice == 'scissors') or
    (choice == 'paper' and computer_choice == 'rock') or
    (choice == 'scissors' and computer_choice == 'paper')):
    prompt('You win!')
elif ((choice == 'rock' and computer_choice == 'paper') or
      (choice == 'paper' and computer_choice == 'scissors') or
      (choice == 'scissors' and computer_choice == 'rock')):
    prompt('Computer wins!')
else:
    prompt('It\'s a tie!')