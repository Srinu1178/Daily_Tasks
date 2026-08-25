# Problem 7: Memory Address
# Task: Create two variables pointing to the same integer. Print id() of both.
# Example Input:
# a=100,b=a
# Example Output:
# Same id values
a = 100
b = a
if id(a)==id(b):
    print("Same id values")