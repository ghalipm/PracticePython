"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can tell if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""


def eligible_to_vote(age, citizenship):
    if age >= 21 and citizenship == "USA":
        return "You are eligible to vote!"
    else:
        return "You are not eligible to vote!"


print(eligible_to_vote(19, 'USA'))

score = 85


def calculate_grade(scores):
    if 0 <= scores <= 100:
        if scores >= 90:
            return "A"
        elif scores >= 80:
            return "B"
        elif scores >= 70:
            return "C"
        elif scores >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Invalid score!"


print("Your letter grade is", calculate_grade(score) if 0 <= score <= 100 else "Invalid score!")

n1 = -2


def classifier(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


print(classifier(n1))

str1 = "racecar"


def is_palindrome(string):
    return string == ''.join(reversed(string))


# The reversed() function returns a reversed iterator, not a reversed string.
# To compare it with the original string, you need to convert it back to a string.

print(is_palindrome(str1))


def is_palindrome2(string):
    return string == string[::-1]
    # str slicing


str1 = "racecar"  # Example palindrome string
print(is_palindrome2(str1))
