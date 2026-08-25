# Problem 12: Roll Number Check
# Task: Length must be exactly 10.
# Example Input:
# AB12345678
# Example Output:
# Valid
roll_number = input("Enter Your Roll No: ")
if len(roll_number)==10:
    print("Valid")
else:
    print("Invalid")