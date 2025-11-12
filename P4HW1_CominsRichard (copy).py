import math

#P4HW1

#Richard Comins
#10/31/2025
#P4HW1_CominsRichard.py
#This program assess the user"s understanding of loops and how they contribute to the IPO process

#Create a list to hold the elements of the grades for each iteration.
scores = []     #used to hold valid scores
num_scores = int(input("How many scores do you want to enter? "))

#Ask the user to declare how many scores/grades the list will contain
for i in range(num_scores): 
    score = float(input(f"Enter score #{i + 1}: "))
    while score < 0 or score > 100:
        print("\nINVALID score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1}: "))
    scores.append(score)

#Process the datal(s
lowest_score = min(scores)
scores.remove(lowest_score)
average = sum(scores) / len(scores)

#Determine letter grade
if average >= 90:
    grade = "A"

elif average >= 80:
    grade = "B" 

elif average >= 70:
    grade = "C"

elif average >= 60:
    grade = "D" 

else:
    grade = "F"

#Display results ("Output")
print("_" * 16 + "Results" + "_" * 16)
print(f"{'Lowest score:':20}{lowest_score:.2f}")
print(f"{'Modified List:':20}{scores}")
print(f"{'Average:':20}{average:.2f}")
print(f"{'Letter grade:':20}{grade}")
print("_" * 50)
print()

#
#     \n__________Results__________")
#print(f"{'Lowest score score:':20)":{loest_score:.2f}"))

#total_sum = sum(scores)
#num_elements = len(scores)
#average = total_sum / len(grades)


#Ask the user how many scores to enter.
#num_scores = int(input("Enter the number of scores you want to enter:"))

#Ask the user for a score to enter.
#for count in range (num_scores):
#    score = float(input(f"Enter score #{count+1}: "))    
#    while score < 0 or score > 100:
#        #print("INVALID Score entered!!!!    ")
#        print("INVALID Score entered!!!!    ")
#        print(str("Score should be between 0 and 100"))
#        score = float(input(f"Enter score #{count+1}: "))
#    #Add the values of the mod_scores_list
#    
#
#print(scores)                      
#
#print()
#print("-" * 16 + "Results" + "-" * 16)
#print()
#print(f{Lowest Score}core}"Lowest Score:")
#print("Lowest score:",min((score)))
#print(scores)
#print(mod_scores)
#
#Define the variables
###min_score = min(scores)
#Remove lowest
#scores.remove(min_score)
#total_sum = sum(scores)
#num_elements = len(scores)
#average = total_sum / len(scores)
#len = sum(scores) 
#modified_list = scores
#print(f"{'Lowest score:  '}{min_score:>25.2f}")
#print(scores)
#print(f'{Modified List',: :}{scores}:>35))
#print(f"{'Lowest score:  '}{min_score:>25.2f}")
#print(f"{'Modifiesd List:'}{scores:>25.2f}")
#print(f"{'Highest score: '}{max(scores):>25.2f}")
#print(f"{'Sum of scores: '}{total_sum:>25.2f}")      
#print(f"{'Average:       '}{average:>25.2f}")
#print()
#print("-" * 50)
###