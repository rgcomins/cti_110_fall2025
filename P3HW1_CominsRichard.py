import math
#P3HW1_CominsRichard
 
#Richard Comins
#10/11/2025
#This program converts and displays #numbered grade to a letter grade
#it then calculates and displays:maximum grade,minimum grade,and average grade

# Enter grades for six modules

mod_1_grade = float(input('Enter grade for Module 1: '))
mod_2_grade = float(input('Enter grade for Module 2: '))
mod_3_grade = float(input('Enter grade for Module 3: '))
mod_4_grade = float(input('Enter grade for module 4: '))
mod_5_grade = float(input('Enter grade for module 5: '))
mod_6_grade = float(input('Enter grade for module 6: '))

#Create an empty list named "grades"
grades = []

#Create a list named "module_grades"
module_grades = [mod_1_grade,mod_2_grade,mod_3_grade,mod_4_grade,mod_5_grade,mod_6_grade]

#Check to see if both lists were created correctly
print(grades)
print(module_grades)
print()
#Combine the two lists by adding the "module_grades" list to the "grades" list.
grades.extend(module_grades)
#Check to see if module_grades list  was incorpeoated into the grades 
print()
print(grades)
print(module_grades)

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
len = len(grades)
average = sum / len


# determine letter grade for average
print()
print()
print("----------------RESULTS----------------")
print()

if average  >= 90:

    print("Your grade is: A ")
elif average >= 80:
    print("Your grade is: B ")
elif average >= 70:
    print("Your grade is: C ")
elif average >= 60:
    print("Your grade is: D ")
else:
    print("Your grade is: F ")
      
#     DO: finish this
print()
print(f"{'Highest Grade is: ':<30}{max(grades):>6.2f}")
print(f"{'Lowest Grade is: ':<30}{min(grades):>6.2f}")
print(f"{'Sum of Grades is: ':<30}{sum:>6.2f}")
print(f"{'length of Grades is: ':<30}{len:>6.2f}")
print(f"{'Average is: ':<30}{average:>6.2f}")
print("-" * 50)
      





