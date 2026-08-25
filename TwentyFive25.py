# Problem 25: Secret Code Verification
# Task: If first three chars are ABC print Verified else Rejected.
# Example Input:
# ABC7845
# Example Output:
# Verified
code = input("Enter Your Code: ")
if code[:3] == 'ABC':
    print("Verified")
else:
    print("Rejected")