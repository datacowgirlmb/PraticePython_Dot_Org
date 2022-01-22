# Ex 4: Divisors

number = int(input("Enter an integer: "))

divisors = []

for i in range(1, number+1):
  if number % i == 0:
    divisors.append(i)

print("Divisors of ", number, ":", divisors)
