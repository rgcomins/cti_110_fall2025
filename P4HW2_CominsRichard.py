#Richard Comins
#10/16/2025
#P4HW2
#Exercise in frustration--Formatting niceities

# pseudocode
"""
# Get name from the user
# while name != "Done"
    #Get hours worked,pay rate,over time rate from the user
    #if hours_worked > 40:
        # calculate with overtime
    else:
        # calculate with no overtime
    # add to total
    # print results
    # get the next name from the user
    # end While
# print the totals
"""


#Get your first name and last name from the user
name = input("Enter employee name or 'Done' to end: ")
count = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while name != "Done":

    count = count + 1
    
    print()
    #Get hours worked,pay rate,over time rate from the user
    hours_worked = float(input('Enter the number of hours worked: '))
    regular_pay_rate = float(input('Enter the pay rate: '))
    regular_pay = float(regular_pay_rate * hours_worked)
    #Decision structure to determine which pay rate to use in calculations

    if hours_worked > 40:
        # calculate with overtime
        over_time_hours = hours_worked-40 
        over_time_pay_rate = regular_pay_rate * 1.5
        name = over_time_pay = over_time_hours * over_time_pay_rate
        regular_pay = regular_pay_rate * 40
        gross_pay = regular_pay + over_time_pay
    else:
        # no overtime
        over_time_hours = 0
        over_time_pay = 0
        regular_pay = regular_pay_rate * hours_worked
        gross_pay = regular_pay + over_time_pay
    # add to total
    total_overtime_pay += over_time_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # print results
    print("-" * 30)   
    print("employee name:",name)
    print(f"{'Hours Worked':15}{'Pay Rate':16}{'OverTime':15}{'OT Pay':16}{'Reg Hour Pay':16}{'Gross Pay':16}")
    print("-"*90) # prints a line
    print(f"{hours_worked:<15.2f}${regular_pay_rate:<15.2f}{over_time_hours:<15.2f}${over_time_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}")
    #print(hours_worked,regular_pay_rate,over_time_hours, over_time_pay, regular_pay,gross_pay)

    print()
    print()
    # get the next name from the user
    name = input("Enter employee name or 'Done' to end: ")
# end of loop
# print totals
print()

print(f"Total employees: {count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")