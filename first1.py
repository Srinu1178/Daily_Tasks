# Problem 1: Safe Division
# Task: Read two integers. If the second is not 0, print the quotient; otherwise print
# Cannot Divide.
# Example Input:
# 20
# 4
# Example Output:
# # 5.0
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
if num2>0:
    print(num1/num2)
else:
    print("Cannot Divide")