import math

#P2HW2_CominsRichard

#Richard Comins
#09/27/2025
#P2HW2
#This program assess the user"s understanding of Lists

#Create a list to hold the elements of the grades for each module.
grades = []

#Ask he user for the grade of each module.

module_1_grade = float(input("Enter the grade for Module 1: "))
module_2_grade = float(input("Enter the grade for Module 2: "))
module_3_grade = float(input("Enter the grade for Module 3: "))
module_4_grade = float(input("Enter the grade for Module 4: "))
module_5_grade = float(input("Enter the grade for Module 5: "))
module_6_grade = float(input("Enter the grade for Module 6: "))

#Create a list to hold the grades for all modules
mod_grades=[module_1_grade,module_2_grade,module_3_grade,module_4_grade,module_5_grade,module_6_grade
             
             ]

#Add the values of the mod_grades list to the grades list
grades = grades.append ((mod_grades))
print()
print("-" * 16 + "Results" + "-" * 16)
print()
#print("Lowest Grade:",min((grades)))
