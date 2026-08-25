# Problem 14: Password Strength
# Task: Length >=12.
# Example Input:
# StrongPass12
# Example Output:
# Strong Password
password = input("Enter Your password: ")
if len(password)>=12:
    print("Strong Password")
else:
    print("Not Strong Password")