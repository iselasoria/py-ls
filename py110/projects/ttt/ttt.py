import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'


def prompt(message):
    print(f'==> {message}')


def display_board(board):
    os.system('clear')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def empty_squares(baord):
    return [key
            for key, val in board.items()
            if val == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return False

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square {", ".join(valid_choices)}:')
        square = input().strip()
        if square in valid_choices:
            break

        prompt('Sorry, that\'s not a valid choice: ')
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER


board = initialize_board()
display_board(board)

while True:
    player_chooses_square(board)
    display_board(board)

    computer_chooses_square(board)
    display_board(board)

    if someone_won(board) or board_full(board):
        break
