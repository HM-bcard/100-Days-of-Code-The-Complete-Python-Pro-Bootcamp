names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
name_len = len(names)
name_number = random.randint(0,name_len-1)
random_name = names[name_number]

print(f"{random_name} is going to buy the meal today!")