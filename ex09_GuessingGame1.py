# Ex 9: Guessing Game 1

# Randomly generate a number between 1 & 9
# Have user guess
# Tell user whether guess was right, too high, or too low

import random

number = random.randint(1, 10)

guess = int(input('Guess which number the computer select (1-9): '))

while guess != number:
    if guess > number:
        print('Too HIGH! Guess again.')
    else:
        print('Too LOW! Guess again.')

    guess = int(input('Next guess: '))
else:
    print('You go it right!')
