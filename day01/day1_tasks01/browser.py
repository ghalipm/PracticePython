"""
20. Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, output should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""
browser_name = str(input("Enter browser name:"))
browser_list = {"Chrome", "Firefox", "Opera", "Safari", "Edge"}

print(f"{browser_name} Browser is selected" if browser_name in browser_list else "Invalid Browser Name")
