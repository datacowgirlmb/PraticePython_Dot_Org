# Ex 2: Odd or Even

number = int(input("Enter an integer: "))

if number == 0:
    print('The number', number, 'is neither odd nor even.')
elif number % 4 == 0:
    print('The number', number, 'is a multiple of 4.')
elif number % 2 == 0:
    print('The number', number, 'is even.')
else:
    print('The number', number, 'is odd.')
