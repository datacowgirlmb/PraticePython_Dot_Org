# Ex 13: Fibonacci
# Ask user for length of list, & return a list of fibonacci numbers

def get_fibonacci(list_length):
    fibonacci = [1, 1]

    for i in range(list_length-2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    return fibonacci
    
length = int(input('How long would you like your Fibonacci sequence to be? '))

while length < 2:
    print('List length must be greater than 1.')
    length = int(input('How long would you like your Fibonacci sequence to be? '))

fib = get_fibonacci(length)
print('Your Fibonacci list:', fib)
