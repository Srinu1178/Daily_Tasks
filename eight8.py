# Problem 8: Memory Comparison
# Task: Compare id() of two variables storing the same string.
# Example Input:
# x='Hi', y='Hi'
# Example Output:
# Same Address / Different Address
x = 'Hi'
y = 'Hi'
if id(x)==id(y):
    print("Same Address")
else:
    print("Different Address")