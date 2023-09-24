"""
17. Create a python file named crew_and_passenger, Given a number of people on the ship, determine how many need to be
crew members and how many can be passengers. Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
crew = 0
passenger = 0
number = ""
total = int(input("Enter total number of people:"))
# if 50 <= total <= 100:
if total in {50, 75, 100}:
    if total % 25 == 0:  # 50, 75, 100
        if total % 100 == 0:  # 100
            crew = 30
            passenger = 70
        elif total % 75 == 0:  # 75
            crew = 25
            passenger = 50
        else:  # 50
            crew = 20
            passenger = 30
    else:
        number = "not valid"
else:
    number = "not valid"

print(f"Total {total}: ", f"crew : {crew}, passenger: {passenger}," if 50 <= total <= 100 and (
        total % 100 == 0 or total % 75 == 0 or total % 50 == 0) else f"Number {number}")
