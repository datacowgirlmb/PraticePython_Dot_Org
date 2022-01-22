# Ex 12: List Ends

# Get a list & return the first and last elements

def list_ends(list):
    return(list[0], list[-1])

user_list = input('Enter a list of numbers: ')

print(list_ends(user_list))
