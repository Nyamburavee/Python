class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #list representing a 3x3 board
        current_winner = None

    def print_board(self):
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]: #getting rows
            print('|' + ' |'.join(row) + ' |')


    def print_game_numbers():
        number_board = [[str(i) for i in range[j*3:(j+1)*3]] for j in range(3)]:
        for row in number_board:
            print('|' + ' |'.join(row) + ' |')



class tictactoe:
def __init__(self):
    self.board = [' ' for _ in range(9)]
    current_winner = None

def print_board(self):
    for row in [self.board[i*3: (i+1) *3] for i in range(3)]
    print('|' + ' |'.join(row) + ' |')

def print_game_numbers():
    number_board = [[str(i) for i in range[j*3: (j+1) *3] for j in range(3)]]
    for row in number_board:
        print('|' + ' |'.join(row) + '|')