names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names_len = len(names)
random_choice = random.randint(0,names_len-1)
random_name = names[random_choice]
print(f"{random_name} is going to buy the meal today!")
