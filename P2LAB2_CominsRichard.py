# Richard Comins
# 09 - 23 - 2025
# P2LAB2
# Dictionaries with Cars

carsDict = {
    'Camaro':18.21,
    'Prius':52.36,
    'Model S':110,
    'Silverado':26
}

carsKeys = carsDict.keys()

print(f"{'Car Models: '}{list(carsKeys)}")

print()
carName = input(f'{"Enter a vehicle to see it's mpg: "}')

mpg = carsDict[carName]

print()
print(f"The {carName} gets {mpg} mpg.")

print()
milesTrav = int(input(f'{"How many miles will you drive the "}{carName}{"? "}'))

galNeeded = milesTrav / mpg

print()
print(f"{galNeeded:.2f} gallon(s) of gas are needed to drive the {carName} {milesTrav} miles.")