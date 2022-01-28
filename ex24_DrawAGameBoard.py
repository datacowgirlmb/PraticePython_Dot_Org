# Ex 24: Draw a Game Board

# Draw a square board based on user-entered dimensions.

def horiz_line():
    print(' ---' * squares)

def vertical_line():
    print('|   ' * (squares + 1))

print("Let's draw a square game board!")
squares = int(input('How wide should be the board be? Enter an integer: '))

for i in range(squares):
    horiz_line()
    vertical_line()
horiz_line()
