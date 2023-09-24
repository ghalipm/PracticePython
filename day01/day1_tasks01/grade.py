"""
18. Create a python file named grade, a variable named grade is given.
write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            otherwise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
grade=str(input("Enter your letter grade : "))
grade_list={"A", "B", "C", "D", "F"}
message=""
if grade in grade_list:
    if grade=="A":
        message="excellent"
    elif grade=="B":
        message="great job"
    elif grade == "C":
        message = "good"
    elif grade == "D":
        message = "passed"
    else:
        message="failed"
else:
    message="invalid letter grade. Valid letter grades are : A, B, C, D, F "

print(f" '{grade}' : {message}" if grade in grade_list else f"{message}")
