# Conditional statements or decision making statements
# write a program to check wheather a number even or odd:
num = int(input("Enter a Number: "))
if num%2 == 0:
    print("Number is even")
else:
    print("Number is not even")

# Checking wheather a password is length enough or not
password = input("Enter your password: ")
if len(password)>8:
    print("password has enough characters")
else:
    print("Not lenghthy enough")


# Write a program to withdraw money from my account

withdraw = int(input("Enter the amount: "))
balance = 10000
if withdraw <= balance:
    balance -= withdraw
    print(f'withdraw sucessful and current balance is {balance}')
else:
    print("Not enough balance")

# Write a program check wheather a person login or not
password = input("Enter your password: ")
reg_password = 'Srinu@342'
if password == reg_password:
    print("Login sucessful")
else:
    print("login failed")

# conditional statements with logical operators
empids = [101,102,103,104,105]
fingerprint= input("Enter wheather the fingerprint is valid or not")
emp_id = int(input("Enter employee id: "))
if fingerprint == 'valid' and emp_id in empids:
    print("login successful")
else:
    print("employee doesnot exist")