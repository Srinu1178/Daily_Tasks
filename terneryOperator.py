
# # write a ternary to check wheather a number is divisible by 3 or not

# num = int(input("Enter the number: "))
# value = 'divisible by 3' if num%3==0 else 'not divisible by 3'
# print(value)


# # write a ternary to check wheather an order is eligible for free dekivery or not

# price = int(input("Enter the price: "))
# print("Free Delivery") if price>500 else print("Delivery charges applicable")


# # write a ternary to check wheather a number is divisible by 5 but not by 10

# num = int(input("Enter the number:"))
# print("divisible by 5 but not 10" if num%5==0 and num%10!=0 else
#       "num is not divisible by 5")


# -> Ternary does not have elif statement

# marks = int(input("Enter the number: "))
# result = 'Grade A' if marks>90 elif marks>70 'Grade B' else 'Grade c'else
# print(result)

# # nested ternary operator: 

# marks = int(input("Enter the marks: "))
# result = 'Grade A' if marks>90 else "Grade B" if marks>80 else "Grade C" if marks > 50 else "Grade D" 
# "Fail"
# print(result) 

signal = input("Enter color: ")

result = 'stop' if signal == 'red' else 'get ready' if signal=='yellow' else 'start' if signal=='green' else "Invalid"
print(result)


# write a nested ternary to generate electricity bill charge 5 rupees per unit
# if no of units used is less than or equal to 200, charge 8 rupees per unit if no of
# units used is less than or equal to 400 
