student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
  
  value = student_scores[score]
  if value >= 91:
    student_grades[score] = "Outstanding"
  elif value >= 81 and value < 91:
    student_grades[score] = "Exceeds Expectations"
  elif value >= 71 and value <80:
    student_grades[score] = "Acceptable"
  else:
    student_grades[score] = "Fail"


    

# 🚨 Don't change the code below 👇
print(student_grades)