import math

#P2HW2_CominsRichard

#Richard Comins
#09/27/2025
#P2HW2
#This program assess the user"s understanding of Lists

#Create a list to hold the elements of the grades for each module.
grades = []
#total_sum = sum(grades)
#num_elements = len(grades)
#average = total_sum / len(grades)


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
#grades.append (module_1_grade,module_2_grade,module_3_grade,module_4_grade,module_5_grade,module_6_grade)
print()
print("-" * 16 + "Results" + "-" * 16)
print()
#print("Lowest Grade:",min((grades)))
#print(grades)
#rint(mod_grades)

#combine the two lists
grades.extend(mod_grades)

#Define the variables
total_sum = sum(grades)
num_elements = len(grades)
average = total_sum / len(grades)
len = sum(grades) 
print(grades)

print(f"{'Lowest grade in the list: ':<40}{min(grades):<55.2f(grades)}")
#print(f"{'Highest grade in the list: '}{     ",max(grades))      
#print(f"Sum of Grades:     ",sum(grades))
#print(f"Average:          ",average,.2)
print()
print("-" * 50)
