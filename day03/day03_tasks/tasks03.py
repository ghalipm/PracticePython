"""
1. Create a python file named list_practices:

1.1 Write a program that can move all the zeros to the last indexes of ArrayList
   Ex:
   list: [1,0,2,0,3,0,4,0]

    output:  [1, 2, 3, 4, 0, 0, 0, 0]

1.2 write a program that can multiply each odd number by 2
   ex:
    list = [1,2,3,4,5];
    output: [2,2,6,4,10]


1.3 Write a program that can remove all the names "Ahmed" from a list of strings
				Ex:
	                list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

	            output:
	            	["John", "Daniel", "James", "Muhammed"]


1.4 Write a program that can display the palindrome strings from a list of String
Ex:
words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

output:
    Anna
    Level


1.5 Write a program that can display the common elements of two lists:
		Ex:
		list1 = [1,2,3,4,5]
		list2 = [4,5,6,7,8]

		Output:
				4
				5

1.6 Write a program that can remove the duplicated elements from a list
	Ex:
	elements = [1,2,3,4,5,1,2,3,4,5]

	Output:
    	[1, 2, 3, 4, 5]

		Notes: Do Not use Set


1.7 Write a program that can remove string elements from a list if the firt and last characters of the string are same
    ex:
		list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

	output:
		["Lan", "Ebrahim", "Farida"]


1.8  Write a program that can display the unique elements of an arrayList:
	ex:
    	list = [1, 1, 2, 3, 3, 4, 5, 5]

	output:
	    	[2, 4]


2. Create a python file named encapsulation_practice:
		create a class called Item
		    private variables:
		        name, unit_price, quantity

	    Encapsulate all the fields:
		        Conditions:
		            name can not be empty
		            unit price can not be negative
		            quantity can not be negative

        If invalid data are given to set the firled, then make sure to throw an error duribg the runtime.
        	(hint: you can use 'raise RuntimeError('Exception message')')


	    Add a constructor that allows user to set all the fields when the object is created.
            (If the arguments not valid it should not be set to the instances)

	    Methods:
	        calcCost(): returns the total cost
	        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()


3. Create a python file named inheritance_practice:
Create an abstract class named Animal:
Variables: name, breed(final), gender(final),  age, size, color(final)
Encapsulate all the fields
Add a cosntructor that can set all the fields

Methods:
eat() ==> different animals eat different foods
drink() ==> all the animals drink water
toString() ==> to display the full info of the animal


Create the following subclasses of Animal:
Dog
eat(): Dog Food

Cat
eat(): Cat Food

Parrot
eat(): Eagle
Displaying 1695215245435-practice_tasks3.txt.

"""
