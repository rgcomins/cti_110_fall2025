#Richard Comins
#10/16/2025
#P3HW2
#Exercise in frustration--Formatting niceities

#Get your first name and last name from the user
fname = input("Enter uour first name: ")
lname = input("Enter your last name: ")
name = fname + " " + lname
print()
#Get hours worked,pay rate,over time rate from the user
hours_worked = float(input('Enter the number of hours worked: '))
regular_pay_rate = float(input('Enter the pay rate: '))
regular_pay = float(regular_pay_rate * hours_worked)
#Decision structure to determine which pay rate to use in calculations

if hours_worked > 40:
   over_time_hours = hours_worked-40 
   over_time_pay_rate = regular_pay_rate * 1.5
   over_time_pay = over_time_hours * over_time_pay_rate
   regular_pay = regular_pay_rate * 40
   gross_pay = regular_pay + over_time_pay
   print(name)
   print(hours_worked,regular_pay_rate,over_time_hours,over_time_pay,regular_pay,gross_pay)
else:
   print(f'name:':<25
   print(hours_worked,regular_pay_rate,regular_pay)
 