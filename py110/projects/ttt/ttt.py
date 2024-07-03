def prompt(message):
    print(f'==> {message}')


def display_board(board):
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
    return {square: ' ' for square in range(1,10)}

def player_chooses_square(board):
    # valid squares
    empty_squares = [key for key, val in board.items() if val == ' ']

    while True:
        valid_choices = [str(num) for num in empty_squares]
        prompt(f'Choose a square {", ".join(valid_choices)}:')
        square = int(input().strip())
        if square in empty_squares:
            break

        prompt('Sorry, that\'s not a valid choice: ')
    board[square] = 'X'



board = initialize_board()
display_board(board)

player_chooses_square(board)
display_board(board)