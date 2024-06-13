print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age?\n"))
if height > 120:
    
    if age >= 18:
            print("Can ride")
    else:
        print("can't ride due to age")
elif height < 120:
    print("Can't ride")
else:
    print("Please input a correct value")

if height%2 == 0:
    print("This is an even number")
elif height % 2 != 0:
    print("This is an odd number")
