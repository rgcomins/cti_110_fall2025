#Richard Comins
#09/18/20025
#P1HW2_CominsRichard
#This program calculates and displays travel expenses.

#Ask user to enter their budget.
travel_budget = float(input("Enter your travel budget: "))

#Ask the user to enter their travel destination.
name = input("Enter your travel destination: ")

#Ask the user how much they will spend on gas.
gas_expenature = float(input("Enter the amount you spent on gas: " ))

#Ask the user how much the accomodations will cost.
accomommodation_expense = float(input("Enter the amount of accommodation expense: "))

#Ask the user to enter how much they spent on food.
food_expense = float(input("Enter the amount spent on food: "))

#calculate total expenses.
total_expenses = gas_expenature + accomommodation_expense + food_expense

#Change travel_expenses to a list.
#total_expenses = list(float(total_expenses))
#total_expense = float(total_expense)



#calculate remaining ballance.
Remaining_Balance = travel_budget - total_expenses
#Display results>
print()
print()
print("---------------Travel Expenses---------------")
print(f"{'Location:':<34} {name} ")
print(f"{'Initial Budget:':<35}${travel_budget:.2f}")
print(f"{'Fuel:':<35}${gas_expenature:.2f}")
print(f"{'Accommodation:':<35}${accomommodation_expense:.2f}")
print(f"{'Food:':<35}${food_expense:.2f}")
print("-------------------------------------------")
print(f"{'Remaining_Balance:':<35}${Remaining_Balance:.2f}")
