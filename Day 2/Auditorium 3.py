age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_int = int(age)
age_weeks_int = int(age_int*52)
ninety_years_weeks = int(90*52)
weeks_left = int(ninety_years_weeks - age_weeks_int)
print(f"You have {weeks_left} weeks left.")
