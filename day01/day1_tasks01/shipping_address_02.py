"""
10. Create a python file named shipping_address
            Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""
name = str(input("Enter your full name: \n"))
building_number = str(input("Enter your building name: \n"))
street_name = str(input("Enter your street name: \n"))
city = str(input("Enter your city name: \n"))
state = str(input("Enter your state name: \n"))
zip_code = int(input("Enter your zipcode: \n"))

print("Your shipping address is:\n", name, "\n", building_number, street_name, "\n",  city, ",", state, zip_code)
