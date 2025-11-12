# While Loops
# As the developer, we do NOT always know how
# how many times the loop will iterate


# While loops are usually controlled by a variable
# Sometimes they are controlled by user
'''
run_program = "yes"

while run_program == "yes":
    print("Program is running...")
    print("🏃🏃🏃🏃🏃")
    
    # Allow user to give new value for run_program
    run_program = input("Should we run the program again? ")
    run_program = run_program.lower()
    
# Loop has broken
print("Program has ended")
'''
# While loop that runs until condition is met

num_of_runs = 6

while num_of_runs >= 0:
    print("Do Something ❤️❤️❤️")
    print(num_of_runs)
    # Decrement num_of_runs by one
    #num_of_runs = num_of_runs - 1
    num_of_runs -= 1
print()
print("We are done looping!!!!")