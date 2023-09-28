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

    8.3 Ask the user would you like to continue (when?: If user enters an invalid entry)
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Grade Calculator APP"

            If user enters an invalid entry, ask the user to re-enter until user provides a valid entry
"""
import numbers

# 8.1:

# option 1:

p_score = int(input("Enter your percentage score: "))


def is_valid_grade(num: numbers):
    return True if 0 <= num <= 100 else False


# option 2:

# try:
#     score = int(input("Enter your score: "))
# except ValueError:
#     print("Invalid Entry")
#     exit()

# 8.2:

def grader(pscore: numbers):
    if is_valid_grade(pscore):
        if 90 <= pscore <= 100:
            return 'A'
        elif 80 <= pscore <= 89:
            return 'B'
        elif 70 <= pscore <= 79:
            return 'C'
        elif 60 <= pscore <= 69:
            return 'D'
        elif 0 <= pscore <= 59:
            return 'F'
    else:
        return "Invalid Entry"


# print(f"Your grade is: {grader(scores)}")

#  8.3 :

def question_invalid_entry(pscore: numbers):
    if is_valid_grade(pscore):
        print(f"Your letter grade: {grader(pscore)}")
        exit()
    else:
        print("Invalid Entry!")
        message = input(" Would you like to continue?")

        while message.lower() == "yes":
            new_score = int(input("Enter your score: "))
            if is_valid_grade(new_score):
                print(f"Valid Entry!{new_score}")
                print(f"Your letter grade: {grader(new_score)}")
                exit()
            else:
                print("Invalid Entry!")
                message = input(" Would you like to continue?")

        if message.lower() == "no":
            print("Thank you for using Grade Calculator APP")
            exit()

        while message.lower() not in {"yes", "no"}:
            print("Invalid Entry!")
            message = input(" Would you like to continue?")

            if message.lower() == "no":
                print("Thank you for using Grade Calculator APP")
                exit()

            elif message.lower() == "yes":
                new_score = int(input("Enter your score: "))
                if is_valid_grade(new_score):
                    print(f"Valid Entry : {new_score}")
                    print(f"Your letter grade: {grader(new_score)}")
                    exit()
                else:
                    print("Invalid Entry!")
                    message = input(" Would you like to continue?")

            else:
                print("Invalid Entry!")
                message = input(" Would you like to continue?")


print(question_invalid_entry(p_score))
