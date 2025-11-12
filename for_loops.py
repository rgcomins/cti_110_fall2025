# Learn to use for loops
# For loop, we as the developer KNOW how many
# times the loop will run

# Make a loop that prints 5 times
# item is a variable, you name it
'''
for item in range(5):
    print("😊")
    print(f"The current value of item is {item}")
    print()
    print()
'''
# Goes up to, but not incuding the ending value
#for cats in range(2,11):
    #print(cats)
    
# Goes up to, but not incuding the ending value
# Add in a step-value
#for cats in range(2,11,2):
    #print(cats)
    
# Use a for loop to get 4 names from user
# Add them into a list
'''
# Create an empty list
friend_names = []

for i in range(4):
    # Get a name from user
    name = input("Gimme a friend's name: ")
    # Append the name into the list
    friend_names.append(name)
    print()
print(friend_names)
'''

# Create a list with values
colors = ["blue", "green", "red", "yellow"]

print(colors)

# Loop though the list of colors
for color in colors:
    print(f"One of the colors is {color}")


    
