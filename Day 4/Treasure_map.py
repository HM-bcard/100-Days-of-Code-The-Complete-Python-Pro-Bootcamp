line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position_split = position.split() # position split splits string into a list
if position_split[0][0] == 'A' and position_split[0][1] == '1':
  line1[0] = 'X' 
elif position_split[0][0] == 'A' and position_split[0][1] == '2':
  line2[0] = 'X' 
elif position_split[0][0] == 'A' and position_split[0][1] == '3':
  line3[0] = 'X' 
elif position_split[0][0]== 'B' and position_split[0][1] == '1':
  line1[1] = 'X' 
elif position_split[0][0] == 'B' and position_split[0][1] == '2':
  line2[1] = 'X' 
elif position_split[0][0] == 'B' and position_split[0][1] == '3':
  line3[1] = 'X' 
elif position_split[0][0] == 'C' and position_split[0][1] == '1':
  line1[2] = 'X' 
elif position_split[0][0] == 'C' and position_split[0][1] == '2':
  line2[2] = 'X' 
elif position_split[0][0] == 'C' and position_split[0][1] == '3':
  line3[2] = 'X' 
else:
  print('Wrong input!')

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
