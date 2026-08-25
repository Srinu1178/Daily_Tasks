# Problem 11: Username Validation
# Task: If length >=8 print Valid Username else Invalid Username.
# Example Input:
# developer
# Example Output:
# Valid Username
username = input("Enter your username: ")
if len(username)>=8:
    print("Valid Username")
else:
    print("Invalid Username")