age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_int = int(age)
age_days_int = age_int * 365
age_weeks_int = int(age_int/7)
ninety_years_weeks = int(90*365/7)
weeks_left = int(ninety_years_weeks-age_weeks_int)
print(f"You have {weeks_left} weeks left")
