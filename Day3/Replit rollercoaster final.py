print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
age = int(input("What is your age?\n"))
bill = 0
if height > 120:
    print("Can ride")
    if age <12:
        bill = 5
        print("The child fee is 5 usd")
    elif age < 18:
        bill = 7
        print("The youth fee is 7")
    else:
        bill = 100
        print("The full fee is 100 usd")
    
    wants_photo = input("Do you want a photo taken Type 'Y' or 'N' ?")
    if  wants_photo == 'Y':
        bill += 3
    #else:
       # bill = bill
    print(f"Your final bill is {bill}")
elif height < 120:
    print("Can't ride")
else:
    print("Please input a correct value")

