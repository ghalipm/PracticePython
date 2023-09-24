"""
3. Create a python file named ShippingAddress. Declare the following variables:
                    name
                    building_number
                    street_name
                    city
                    state
                    zip_code

    Use concatenation to print the full shipping address

        Ex:
            Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""
# shipping_address.py

# Declaration
name = ""
building_number = ""
street_name = ""
city = ""
state = ""
zip_code = ""

# Given Data
name = "Aaron Kissinger"
building_number = "13621A"
street_name = "Legacy Circle"
city = "Fairfax"
state = "VA"
zip_code = "22030"

# Print the full shipping address using concatenation
print("Your shipping address is:")
print(name)
print(building_number + " " + street_name)
print(city + ", " + state + " " + zip_code)

print("--------------------------------")

score = 75
result = None
if 0 <= score <= 100:
    if score >= 60:
        result = "Passed"
    else:
        result = "Failed"
else:
    result = "Invalid"

print(result)
print("**********************************")
score = -45
grade = ""
if 0 <= score <= 100:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
else:
    grade = "Invalid input"

print(grade)
