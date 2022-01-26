# Ex 16: Password Generator

import string
import random


def generate_password(length):
    char_set = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(char_set, length))

    return password

length = int(input('How long would you like your password to be? '))
print('Your password:', generate_password(length))
