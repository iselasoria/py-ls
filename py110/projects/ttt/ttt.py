import random
import os

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'


def prompt(message):
    print(f'==> {message}')

def joinor(opt):

    if len(opt) >= 2:
        return f'Choose a square: {", ".join(opt[:-2])} or {opt[-1]}'
    elif len(opt) == 1:
        return f'Choose a square: {opt}'
    else:
        return f'Choose a square: {""}.'


def display_board(board):
    os.system('clear')

    prompt(f'You\'re {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')
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

def empty_squares(board):
    return [key
            for key, val in board.items()
            if val == INITIAL_MARKER]

def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        # prompt(f'Choose a square {", ".join(valid_choices)}:')
        prompt(f'Choose a square {joinor(valid_choices)}')
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

def detect_winner(board):
    winning_lines = [
        [1,2,3], [4,5,6], [7,8,9],
        [1,4,7], [2,5,8], [3,6,9],
        [1,5,9], [3,5,7]
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def play_ttt():
    while True:
        board = initialize_board()
        # display_board(board)

        while True:
            display_board(board)
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break


        if someone_won(board):
            prompt(f'{detect_winner(board)} won!')
        else:
            prompt('It\'s a tie!')

        prompt('Do you want to play again (y/n)')
        answer = input().lower()

        if answer[0] != 'y':
            break
    prompt('Thanks for playing Tic Tac Toe!')

play_ttt()