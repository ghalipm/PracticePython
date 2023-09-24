"""
2. create a python file named FlightTicket, and declare the following variables:
                1. from
                2. to
                3. ticketPrice

    use concatenation to display the full info of the ticket

    ex:
            Given Data:
                from = "Las Vegas"
                to = "McLean"
                ticket_price = 425.5

            Output:
                From Las Vegas to McLean is $425.5
"""
# flight_ticket.py
# Declare variables
from_location = ""
to_location = ""
ticket_price = 0.0

# Given Data
from_location = "Las Vegas"
to_location = "McLean"
ticket_price = 425.5

# Display the ticket information using concatenation
ticket_info = "From " + from_location + " to " + to_location + " is $" + str(ticket_price)
print(ticket_info)