# Ex 23: File Overlap

# Read two files (one with prime numbers, the other with happy numbers).
# Compare numbers in each & return a list of common numbers.

# Get list of prime numbers
with open('PrimeNumbers.txt', 'r') as open_file:
    primes = open_file.read()

# Get list of happy numbers
with open('HappyNumbers.txt', 'r') as open_file:
    happy = open_file.read()

# Split lists at each carriage return
primes = primes.split('\n')
happy = happy.split('\n')

# Convert list elements from string values to integers
primes = list(map(int, primes))
happy = list(map(int, happy))

list_overlap = []
for prime in primes:
    if prime in happy:
        list_overlap.append(prime)

print(list_overlap)
