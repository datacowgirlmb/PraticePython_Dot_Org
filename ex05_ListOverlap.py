# Ex 5: List Overlap

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

a = []
b = []

for i in range(0,10):
    a.append(random.randint(1, 30))
    b.append(random.randint(1, 30))

ab = [i for i in a if i in b]

print('a:', a)
print('b:', b)
print('Elements in both lists:', ab)
