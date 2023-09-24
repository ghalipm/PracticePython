"""
4. Create a python file named Square, write a program that can calculate the area & perimeter of any given square

        Hint: side need to be given to calculate the area and perimeter of square
            Ex:
                Given Data:
                    side = 5

                output:
                    Area of the square is equal to 25
                    Perimeter of square is equal to 20
"""
# square.py

# Declaration
# side = float(input('Enter side length of the square: \n'))
side = int(input('Enter side length of the square: \n'))
print(side)
area = side * side
perimeter = 4 * side

print("Area of the square is equal to ", area)
print("Perimeter of square is equal to ",  perimeter)
