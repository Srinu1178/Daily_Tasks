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


# elif : elif is used when we have multiple conditions to check and we don't have
# to check remaining condition when one condition turned to be true.
#traffic signal checking using elif
color = input("Enter signal color: ")
if color == 'red':
    print('Stop')
elif color == 'yellow':
    print('Start Your Engines')
elif color == 'green':
    print('Go')
else:
    print('Invalid color')

# assigning grades based on the marks
marks = int(input("Enter students marks: "))
if marks >=950:
    print('You got O Grade')
elif marks>=850:
    print("You got A Grade")
elif marks>=750:
    print("You got B Grade")
elif marks>=650:
    print("You got C Grade")
else:
    print("Try again")


# calculate tax a employee need to pay based on the salary
salary = int(input("Enter your annual salary: "))
if salary<=300000:
    print('No Tax')
elif salary<=500000:
    print(f'you need to pay: {salary*0.05}')
elif salary<=1000000:
    print(f'you need to pay:{salary*0.1}')
else:
    print(f'you need to pay:{salary*0.12}')


# Write a program to print the notification we get based on batter percentage

battery=int(input('Enter your battery percentage: '))
if battery==100:
    print("Full Charge")
elif battery<=10:
    print("Please keep in charge")
elif battery<=20:
    print("Turn on ultra Battery saver")
elif battery<=30:
    print("Turn on battery ")


#write a program to give discount to customer based on the
# amount of bill they made on shopping
# >=10000 5% discount ,>5000 3% discount else no discount

bill = int(input("Enter Your Bill: "))
if bill >=10000:
    print(f'you got 5% discount:{bill*0.05}, You will pay:{bill-(bill*0.05)}')
elif bill >=5000:
    print(f'you got 3% discount:{bill*0.03},you will pay:{bill-(bill*0.03)}')
else:
    print(f"No discount You will pay: {bill}")
