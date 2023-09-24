"""
8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

    8.2 Display the grade of the student.
                    90 ~ 100 ==> A
                    80 ~ 89 ==> B
                    70 ~ 79 ==> C
                    60 ~ 69 ==> D
                    0 ~ 59 ==> F

    8.3 Ask the user would you like to continue
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Grade Calculator APP"

            If user enters an invalid entry, ask the user to re-enter until user provides a valid entry
"""
# 8.1:
# option 1:
scores = int(input("Enter your score:"))
print(" " if 0 <= scores <= 100 else "Invalid Entry")

# option 2:

# try:
#     score = int(input("Enter your score: "))
# except ValueError:
#     print("Invalid Entry")
#     exit()

# 8.2:

try:
    score = int(input("Enter your score: "))
except ValueError:
    print("Invalid Entry")
    exit()
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
elif 0 <= score <= 59:
    grade = 'F'
else:
    print("Invalid Entry")
    exit()

print(f"Your grade is: {grade}")

#  8.3 :
message2 = input(" Would you like to continue?")
if message2 == "yes":
    score = int(input("Enter your score: "))
    if 0 <= scores <= 100:
        if scores >= 90:
            grade = 'A'
        elif scores >= 80:
            grade = 'B'
        elif scores >= 70:
            grade = 'C'
        elif scores >= 60:
            grade = 'D'
        else:
            grade = 'F'
    else:
        grade = None
    print(f"Your letter grade: {grade}" if 0 <= scores <= 100 else "Invalid Entry")
elif message2 == "no":
    print("Thank you for using Grade Calculator APP")
else:
    score = int(input("Enter your score:"))
    if 0 <= scores <= 100:
        if scores >= 90:
            grade = 'A'
        elif scores >= 80:
            grade = 'B'
        elif scores >= 70:
            grade = 'C'
        elif scores >= 60:
            grade = 'D'
        else:
            grade = 'F'
    else:
        grade = None
    print(f"Your letter grade: {grade}" if 0 <= scores <= 100 else "Invalid Entry")

# option 2:
# while True:
#     try:
#         score = int(input("Enter your score: "))
#     except ValueError:
#         print("Invalid Entry")
#         continue  # Ask the user to re-enter the score
#
#     if 90 <= score <= 100:
#         grade = 'A'
#     elif 80 <= score <= 89:
#         grade = 'B'
#     elif 70 <= score <= 79:
#         grade = 'C'
#     elif 60 <= score <= 69:
#         grade = 'D'
#     elif 0 <= score <= 59:
#         grade = 'F'
#     else:
#         print("Invalid Entry")
#         continue  # Ask the user to re-enter the score
#
#     print(f"Your grade is: {grade}")
#
#     choice = input("Would you like to continue (yes/no)? ").lower()
#     if choice != "yes":
#         print("Thank you for using Grade Calculator APP")
#         break  # Exit the loop if the user enters anything other than "yes"
