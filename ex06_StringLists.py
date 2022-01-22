# Ex 6: String Lists

str = input("Enter a string of characters: ")

limit = int(len(str) / 2)

palindrome = True

for char in range(limit):
  if str[char] != str[(char + 1) * -1]:
    palindrome = False
    break

if palindrome == False:
  print("The string you entered is not a palindrome.")
else:
  print("The string you entered is a palindrome.")
