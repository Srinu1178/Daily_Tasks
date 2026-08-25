# Problem 13: Product Code
# Task: Length at least 6.
# Example Input:
# AB1234
# Example Output:
# Accepted
pro_code = input("Enter the product code: ")
if len(pro_code)>=6:
    print("Accepted")
else:
    print("Not accepted")