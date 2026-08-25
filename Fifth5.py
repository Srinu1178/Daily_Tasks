# Problem 5: Discount Eligibility
# Task: Print Free Delivery if bill is at least ₹999; otherwise Delivery Charges Apply.
# Example Input:
# 1250
# Example Output:
# Free Delivery
bill = int(input("Enter the bill: "))
if bill>=999:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")