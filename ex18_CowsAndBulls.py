# Ex 18: Cows & Bulls

# Randmoly generate a 4-digit number.
# Have user guess number.
# For each guess, count 1 cow for each digit in the correct spot,
# & 1 bull for every correct digit in the wrong spot.

import random

def check_guess(number, guess):
    cow = 0
    bull = 0

    # Count bulls
    for i in range(len(guess)):
        if guess[i] in number:
            bull += 1

    # Count cows
    for i in range(len(number)):
        if number[i] == guess[i]:
            cow += 1
            bull += -1

    return cow, bull


if __name__ == "__main__":
    playing = True

    number = str(random.randint(1000,9999))
    #number = str(1234)

    guesses = 0

    print("Let's play Cow/Bull!")
    print("I will pick a four-digit number, and you have to guess it.")
    print("For every correct digit in the right spot, I'll give you a cow.")
    print("For every correct digit in the wrong spot, I'll give you a bull.")
    print('Type "exit" to quit at any time.')

    while playing:
        guess = input("What's your guess? ")
        if guess == "exit":
            print("Nice try! The correct number is " + number + ".")
            break
        cows, bulls = check_guess(number, guess)
        guesses += 1

        print("You've got " + str(cows) + " and " + str(bulls) + " bulls.")

        if cows == 4:
            playing = False
            print("You got it! It took you " + str(guesses) + "! The number was " + number + ".")
            break
        else:
            print("Next guess: ")
