import math
#P3HW1_CominsRichard
 
#Richard Comins
#10/11/2025
#This program converts and displays #numbered grade to a letter grde
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

#Create a list named "mod_grades"
module_grades = mod_1_grade,mod_2_grade,mod_3_grade,mod_4_grade,mod_5_grade,mod_6_grade

# add grades entered to the "grdes" list

grades.extend(module_grades)# = [mod_1 mod2, mod_3, mod_4, Mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
len = len(grades)
average = sum(grades) / len(grades)

# determine letter grade for average


if average  >= 90:

    print("Your grade is: A" )
elif average >= 80:
    print("Your grade is: B" )
elif average >= 70:
    print("Your grade is: C ")
elif average >= 60:
    print("Your grade is: D ")
else:
    print("Your grade is: F ")
      
#     DO: finish this

print("Highest Grade is: ",high)
print("Lowest Grade is: ",low)
