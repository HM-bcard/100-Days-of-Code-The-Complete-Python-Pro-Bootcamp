rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random


#Write your code below this line 👇
users_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computers_hand = random.randint(0,2)
if users_hand == 0:
  print(rock)
elif users_hand == 1:
  print(paper)
elif users_hand == 2:
  print(scissors)
else:
  print('Wrong input.')
  
print(f"Computer chose {computers_hand}:")

if computers_hand == 0:
  print(rock)
elif computers_hand == 1:
  print(paper)
elif computers_hand == 2:
  print(scissors)
else:
  print('Wrong input.')


if users_hand == 0 and computers_hand == 0:
  print('Draw.')
elif users_hand == 1 and computers_hand == 1:
  print('Draw.')
elif users_hand == 2 and computers_hand == 2:
  print('Draw.')
elif users_hand == 0 and computers_hand == 2:
  print('You win.')
elif users_hand == 1 and computers_hand == 0:
  print('You win.')
elif users_hand == 2 and computers_hand == 1:
  print('You win.')
elif users_hand == 0 and computers_hand == 1:
  print('You lose.')
elif users_hand == 1 and computers_hand == 2:
  print('You lose.')
elif users_hand == 2 and computers_hand == 0:
  print('You lose.')
else:
  print('No contest.')
