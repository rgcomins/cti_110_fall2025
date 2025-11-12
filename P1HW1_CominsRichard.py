#Richard Comins
#9/17/2025
#P1HW1_python 
#This program collects information from user, processes information collected and display results to user.



print("-----Calculating Exponents-----\n")



#Ask user to enter an integer which will be used as the base value.

num1 = int(input("Enter an integer as the base value: "))

#Ask user to enter a second number which will be used as the exponent.

num2 = int(input("Enter an integer as the exponent: "))


print(num1,"raised to the power of",num2,"is",num1**num2)

print()
print()


print("-----Additions and Subtractions----\n")



#Ask user to enter an integer to be used as the starting number.

first_num = int(input("Enter an integer as the starting number:  "))

#Ask the user for another interger to be used for addition.

second_num = int(input("Enter another integer as the second number: "))

#Ask the user for another integer to be used for subtraction purposes.
 
third_num = int(input("Enter an integer for subtraction purposes: "))
total = first_num + second_num - third_num

print()
print()
print(first_num,"+",second_num,"-",third_num,"is equal to",total)
