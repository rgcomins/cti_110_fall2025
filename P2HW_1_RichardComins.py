#Richard Comins
#09/25/2025
#P2HW_1
#This program calculates and displays travel expenses
# declare our form strings (never change)
name_location = "Location: "
name_budget   = "Initial Budget: "
name_fuel     = "Fuel: "
name_accom    = "Accommodation: "
name_food     = "Food: "
name_balance  = "Remaining Balance: "
#Ask user to enter their budget.
travel_budget = float(input("Enter your travel budget: "))

#Ask the user to enter their travel destination.
location = input("Enter your travel destination: ")

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
remaining_ballance = travel_budget - total_expenses
#Display results>
print()
print()
print("-"*25,"Travel Expenses","-"*25)

print(f"{name_location:<45}{location:<45}")

print(f"{name_budget:<45}${travel_budget:<45.2f}")

print()
print(f"{name_fuel:<45}${gas_expenature:<45.2f}")
print(f"{name_accom:<45}${accomommodation_expense:<45.2f}")
print(f"{name_food:<45}${food_expense:<45.2f}")
print()
print(f"{name_balance:<45}${remaining_ballance:<45.2f}")


