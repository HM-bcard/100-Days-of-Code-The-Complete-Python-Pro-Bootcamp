#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#letters:
letters1 = ''
numbers1 = ''
symbols1 = ''

for i in range(nr_letters):
  letters1 += str((letters[random.randint(0,len(letters)-1)]))
for i in range(nr_symbols):
  symbols1 += str((symbols[random.randint(0,len(symbols)-1)]))
for i in range(nr_numbers):
  numbers1 += str((numbers[random.randint(0,len(numbers)-1)]))
                  
password1 = (letters1+numbers1+symbols1)
#print(password1)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#print (len(letters))
password1_insides = []
password2 = ''
for i in range (len(password1)):
  password1_insides.append(password1[i])
#print(password1_insides)
# for i in range (random.randint(0,len(password1_insides))):
 # password2 += password1_insides[i]
 # del password1_insides[i]

random.shuffle(password1_insides)
#print(password1_insides)

for char in password1_insides:
  password2 += char 

print(f"Your password is:{password2}")
