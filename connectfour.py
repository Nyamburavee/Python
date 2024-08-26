import numpy as np

ROW_COUNT = 7
COLUMN_COUNT = 6

def create_board():
    board = np.zeros(6,7)
    return board

board = create_board()
print(board)

def is_valid_location(board, row):
    board[5][col] == 0
    
def get_next_open_row(board, row, col):
    for r in range(ROW_COUNT):
        if board[row][col] == 0:
            return r
        
def drop_piece(board, row, col, piece):
    board[row][col] = piece
    return board

def print_board(board):
    print(np.flip(board, 0))


board = create_board()
print_board(board)
Game_over = 0
Turn = 0

while not Game_over:
    if Turn == 0:
        col = int(input('Player one enter you selection: '))
        if is_valid_location(board, row):
            row = get_next_open_row(board, row)
            drop_piece(board, row, col, 1)

    else:
        col = int(input('Player two enter you selection: '))
        if is_valid_location(board, row):
            row = get_next_open_row(board, row)
            drop_piece(board, row, col, 2)

    print_board(board)

    Turn += 1
    Turn = Turn % 2


