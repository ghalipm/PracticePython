"""
5. Create a python file named Rectangle, write a program that can calculate the area & perimeter of any given Rectangle

        Hint: width and length need to be given to calculate the area and perimeter of rectangle
            Ex:
                Given Data:
                    length = 5
                    width = 2

                output:
                    Area of the rectangle is equal to 10
                    Perimeter of rectangle is equal to 20
"""
length = int(input("Enter length of rectangle: \n"))
width = int(input("Enter width of rectangle \n"))

area = width * length
perimeter = 2 * (width + length)

print("Area of the rectangle is equal to ", area)
print("Perimeter of rectangle is equal to ", perimeter)
