
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
pwd_letters = ""
pwd_symbols = ""
pwd_numbers = ""


for i in range(nr_letters):
    pwd_letters += letters[random.randint(0,len(letters)-1)]
for i in range(nr_letters):
    pwd_numbers += numbers[random.randint(0,len(numbers)-1)]
for i in range(nr_letters):
    pwd_symbols += symbols[random.randint(0,len(symbols)-1)]

pwd = pwd_letters+pwd_numbers+pwd_symbols
print(f"Your un-shuffled password is {pwd}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
randomised_pwd= ''
len_pwd = len(pwd)
#pwd_sndom.shuffle(pwd_list)
print(pwd_list)



for i in range(len(pwd_list)):
    randomiplit = pwd.split()
pwd_list = []

for i in range (len(pwd)):
    pwd_list += pwd[i]
print(pwd_list)
rased_pwd += pwd_list[i]

randomised_pwd = str(randomised_pwd)
print(randomised_pwd)
