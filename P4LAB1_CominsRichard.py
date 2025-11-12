#P4LAB1_CominsRichard
#Richard Comins
#10/22/2025
#P4LAB1
#This program draws shapes using for and while loops



import turtle

#Create the turtle drawing object
capri = turtle.Turtle()

#create the window for drawing
window = turtle.Screen()

#change the background color
window.bgcolor("tan")

#change the the turtle color()
capri.color("purple")
capri.fillcolor("purple")
#Draw fill color for cube
capri.begin_fill()
#Draw the square using a for loop

for side in range(4):
    capri.forward(200)
    capri.right(90)
    
capri.end_fill()    
    
#keep the window open
#window.mainloop()


#keep the window open
capri.color("green")
capri.begin_fill()
#while loop to draw the roof
num_runs = 3

while num_runs > 0 :
    #draw a side
    
    capri.forward(200)
    capri.left(120)
    
    
    
    #decrease num-runs so the loop breaks
    num_runs = num_runs-1 
capri.end_fill()    
#keep the window open
window.mainloop()
