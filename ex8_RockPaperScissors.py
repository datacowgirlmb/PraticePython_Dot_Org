from random import randint

# Possible plays
t = ['Rock', 'Paper', 'Scissors']

def play(computer_play, player_play):
    if computer_play == player_play:
        result = 'tie'
        verb = 'ties with'
    else:
        if player_play == 'Rock':
            if computer_play == 'Paper':
                result = 'lose'
                verb = 'covers'
            else:
                result = 'win'
                verb = 'smashes'

        elif player_play == 'Paper':
            if computer_play == 'Rock':
                result = 'win'
                verb = 'covers'
            else:
                result = 'lose'
                verb = 'cuts'

        elif player_play == 'Scissors':
            if computer_play == 'Rock':
                result = 'lose'
                verb = 'smashes'
            else:
                result = 'wins'
                verb = 'cuts'

    return result, verb

def apply_camelcase(words):
    words = words.split(' ')
    return ''.join(word[0].upper() + word[1:].lower() for word in words)

def validate_player_choice(player_choice):
    if player_choice == 'Rock' or player_choice == 'Paper' or player_choice == 'Scissors':
        return True
    else:
        return False

win_lose = 'lose'

while win_lose == 'lose':
    computer = t[randint(0,2)]
    player = input('Rock, Paper, or Scissors? ')

    player = apply_camelcase(player)

    if validate_player_choice(player) == False:
        print(player, 'is an invalid choice.')
        break

    win_lose, action = play(computer, player)

    win_lose_string = 'You ' + win_lose + '!'

    if win_lose == 'lose':
        action_string = computer + ' ' + action + ' ' + player + '. Try again!'
    else:
        action_string = player + ' ' + action + ' ' + computer + '.'

    print(win_lose_string, action_string)
