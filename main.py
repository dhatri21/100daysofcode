#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []
passwords = ""

for nr_letters in range(1,nr_letters+1):
  random_letter = random.randint(1,len(letters))
  password.append(letters[random_letter])

for nr_symbols in range(1,nr_symbols+1):
  random_symbols = random.randint(0,len(symbols)-1)
  password.append(symbols[random_symbols])

for nr_numbers in range(1,nr_numbers+1):
  random_numbers = random.randint(0,len(numbers)-1)
  print(random_numbers)
  password.append(numbers[random_numbers])
  
for n in range(0,len(password)):
  passwords += password[n]

print(passwords)
