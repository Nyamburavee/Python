import random

print('Welcome To Your Password Generator')
chars = 'abcdeefghijklmnopqrstuvwxyzABCDEEFGHIJKLMNOPQRSTUVWXYZ123456789?/#@!$%^&*><'

Number = input('How many passwords do you need?:')
Number = int(Number)

Length = input('Enter password length:')
Length = int(Length)


print('Here are your passwords:')

for pwd in range(Number):
    passwords = ' '
    for c in range(Length):
        passwords += random.choice(chars)

    print(passwords)