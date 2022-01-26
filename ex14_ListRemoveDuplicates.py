# Ex 14: List Remove Duplicates

def remove_duplicates(l):
    return list(set(l))


l = list(input('Enter a list of numbers (separated by commas): '))

print(remove_duplicates(l))
