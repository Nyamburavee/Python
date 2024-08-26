import random

def play():
    user = input('what is your choice? rock(r), paper(p) or scissor(s)')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Its a tie')

    elif is_win(user, computer):
        return 'You won'
    else: 
        return 'You lost'

# r > s, s > p, p > r
def is_win(player, opponent):
    # return true if player wins
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True

print(play())

