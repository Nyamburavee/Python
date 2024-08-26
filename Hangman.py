import random
import string


 #get random word
words = ["Daniel", "Mark", "Ruth"]


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


# define variables
def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    used_letters = set()  # letters that the user has guessed
    alphabet = set(string.ascii_uppercase)
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and have used the following letters: ', ' '.join(used_letters))

        # current word is e.g w-rd
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word is: ', ' '.join(word_list))

        user_letter = input('Enter a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter not in word')

        elif user_letter in used_letters:
            print('You have already used that letter. Try again')
        else:
            print('invalid character')

    if lives == 0:
        print('Sorry you died. You lost')
    else:
        print('You guessed the word.You won!')


hang_man()
