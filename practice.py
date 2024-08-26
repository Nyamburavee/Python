import random

def guess_game(x):
    random_num = random.randint(1, x)
    guess = 0

    while guess != random_num:
        guess = int(input(f'enter a number btwn 1 and {x}:'))
        if guess > random_num:
            print('Your guess is too high. Try again')
        elif guess < random_num:
            print('Your guess is too low. Try again')
    else:
        print('You guessed the number. You won!')


guess_game(10)



'''def computer_guess(x):
    low = 1
    high = x
    feedback = ' '

    while feedback != 'c':
        if low != high:
            guess = random.randit(low, high)
        else:
            guess = high
        feedback = input(f'is {guess} too high(h), too low(l), or correct(c)?').lower()
        if guess == 'h':
            high = guess - 1
        elif guess == 'l':
           low = guess + 1
    print(f'The computer guessed your number {guess} correctly')

computer_guess(30)'''

def play():
    user = input('is your choice rock(r), paper(p) or scissors(s)')
    computer = random.choice('r','p','s')

    if user == computer:
        return 'its a tie'
    
    if is_win(user, computer):
        return 'you won'
    
    return 'you lost'

def is_win(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 's':
        return True
    
print|(play())


def play(x):
    low = 1
    high = x
    feedback = ' '

    while feedback != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = high

            feedback = input('is {guess} too high(h), too low(l), or correct(c)').lower()
            if guess == 'h':
                high = guess - 1
            if guess == 'l':
                low = guess + 1

    print('Yess the comuter guesed your number {guess} right')

play(400)










words = ['Hey', 'Hello', 'Jambo']
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    
def hang_man():
    word = random.choice(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 5

    while len(word_letters) > 0 and lives != 0:
        print('You have', lives,'lives left and and have used the following letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('The current word is: ',' '.join(word_list))

        user_letter = input('Enter a letter: ').upper()
        if user_letter - used_letters:
            used_letters.add(user_letter)
            if user_letter in used_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
        elif user_letter in used_letters:
            print('You have already used this letter')
        else:
            print(' Invalid letter')
    if lives == 0:
        print('Sorry bro!You lost.')
    else:
        print(' You wonnn!')   

hang_man()
