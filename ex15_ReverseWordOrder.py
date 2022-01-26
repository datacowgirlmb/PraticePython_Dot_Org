# Ex 15: Reverse Word Order

def reverse_words(string):
    string = string.split(' ')
    string.reverse()
    string = ' '.join(string)

    return string

phrase = input("Enter a string: ")
phrase = reverse_words(phrase)
print(phrase)
