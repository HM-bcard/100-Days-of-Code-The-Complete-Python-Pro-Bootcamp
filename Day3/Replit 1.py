print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age?\n"))
if height > 120:
    print("Can ride")
    if age <12:
        print("The fee is 5 usd")
    age <= 18:
        print("The fee is 7")
else:
    print("The full fee is 100 usd")
elif height < 120:
    print("Can't ride")
else:
    print("Please input a correct value")

if height%2 == 0:
    print("This is an even number")
elif height % 2 != 0:
    print("This is an odd number")
