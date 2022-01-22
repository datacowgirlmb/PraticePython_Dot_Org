# Ex 3: List Less than 10

limit = int(input('Enter an integer: '))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

a_limit = [i for i in a if i < limit]

print(a_limit)
