#Richard Comins
#9/22/2025
#P2LAB1
#Using math expressions
import math

#Get radius from user
radius = float(input(f"{'Enter the radius: ':<40}" ))

#Calculate the circum, diameter, area
cir = 2 * math.pi * radius 
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display results
print()
print('-'*50)
print()
print(f"{'The diameter of the circle is: ':<40}{diam:.1f}")
print(f"{'The circumference of the circle is: ':<40}{cir:.2f}")
print(f"{'The area of the circle is: ':<40}{area:.3f}")

