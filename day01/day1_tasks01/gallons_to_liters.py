"""
7. Create a class named GallonsToLitters, Write a program that can convert gallon (int) to liter (double)
            Hints: 1 gallon = 3.79 litters
            Ex:
                Given Data:
                     gallon = 10

                output:
                    10 gallon is equal to 37.9 litters
"""
gallon = int(input("Enter number of gallons: \n"))
liter = round(gallon * 3.79, 1)
print(gallon, "gallon is equal to", liter,  "liters")
