# Ex 11: Check Primality Factors

# Ask user for a number, & determine if number is a prime

def get_integer():
    return int(input("Enter an integer: "))


def check_primality(n):
    if (n % 2 == 0):
        if  n != 2:
            is_prime = False
        else:
            is_prime = True

    else:
        for i in range(2, n):
            is_prime = True
            if n % i == 0:
                is_prime = False
                break

    return is_prime

number = get_integer()
prime = check_primality(number)

if prime == False:
    print('The number', number, 'is NOT a prime number.')
else:
    print('The number', number, 'is a prime number.')
