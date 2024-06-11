#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = int(input("Was was the bill amount?:\n"))
no_ppl = int(input("How many people will the bill be split into?\n"))
amount_per_person = round(((bill * 1.12) / no_ppl),2)

print("The amount per person is: " + str(amount_per_person))
