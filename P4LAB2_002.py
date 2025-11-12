# Richard Comins
# 10/23/2025
# P4LAB2
# Used nested loops

# Create variable to control the loop
run_again = "yes"
#trap the user in a while loop, until they give a valid response
while run_again == "yes":
    
    print("Program is running....")
    print()
    #get a number from the user
    num = int(input("Enter an interger "))
    # determine if the num is positive or negative
    
    if num >= 0:
        print("Display multiplication table ")
        print()
        #display num times all the values 
        for i in range(1,13):
            print(f'{num} * {i} = {num * i} ')    
    
    else:
        print("Program does not handle negative numbers")    
    
    
    run_again = input("Would you like to run the program again? ").lower()
    
    print()
    
    
# Loop breaks here
print("Thanks for using the program, Goodbye!")