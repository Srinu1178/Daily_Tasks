#Operator:Operator is a symbol that perform some action between one or 
# more than one objects

#Checking arithmetic operators
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
print(f'Sum of {num1} and {num2} is {num1+num2}')
print(f'Difference of {num1} and {num2} is {num1-num2}')
print(f'Multiplication of {num1} and {num2} is {num1*num2}')
print(f'Division of {num1} and {num2} is {num1/num2}')
print(f'Floor division of {num1} and {num2} is {num1//num2}')
print(f'Modulus of {num1} and {num2} is {num1%num2}')
print(f'{num1} to the power of {num2} is {num1**num2}')

#Assignments operators:These are used to assign a value/object to a
#variable
name="srinu"
# augmented assignment operators
# These are used to perform some operation and assign the result
# the a variable at once
# +=,-=,*=,/=,//=,**=

a = 10
a = a+10
print(a)
a +=10 # This work similar to a = a+10 
print(a)

# Updating score in cricket after evey run
score = 0
score += 6
score += 1
print(score)

# Tracking number of steps walked in a day
step = 0
step += 300
step += 150
step +=78
print(step)

# augmented operator
# deducting bank balance after every transaction
bankBalance = 50000
bankBalance -= 11000
bankBalance -= 2500
bankBalance -= 390
bankBalance -=350
print(bankBalance)

#Battery discharge after every app usage
battery = 100
battery -= 30
battery -= 50
battery -= 19
print(battery)


# Augmented mutiplication 
salary = 50000
# after promotion to get double salary
salary *= 2
print(salary)

#add 10% of price an item 
price = 1299
price *= 1.1
print(price)

#Augmented division
#splitting a bill for 4persons
bill = 5999
bill /= 4
print(bill)

#salary tax deduction
salary1 = 120000
salary1 /= 1.1
print(salary1)

#//= Augmented floor division
# distributed 478 phones among 12 members
iphones = 478
iphones //=12
print(iphones)

#unlocking guns in a game based on points
#such that for every 100 points you get a gun
points = 878
points //=100
print(points)

# %=
# Check wheather a number is even or odd
num = 10
num%=2
print(num)

# getting last digit in a number
num1 = 1234
num1 %= 10
print(num1)

# **=
# calculate the area of square
side = 10
side **=2
print(side)

# Comparison Operators
#Two compare values of two objects they return the boolean value as output
# equal to ==
# Checking whether an employee is admin or not
employee = input("Enter your role: ")
print(employee == 'admin')

#checking given password is equal to save password
savedPass = 'Venkat'
password = input("Enter your Password: ")
print(password==savedPass)

# != not equal to
state = input("Enter a state which is not a capital:")
print(state!='Delhi')

# >=: It Check the value is greater than or nor
age = int(input("Enter your age: "))
print(age>=18)

#Operator:Operator is a symbol that perform some action between one or 
# more than one objects

#Checking arithmetic operators
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
print(f'Sum of {num1} and {num2} is {num1+num2}')
print(f'Difference of {num1} and {num2} is {num1-num2}')
print(f'Multiplication of {num1} and {num2} is {num1*num2}')
print(f'Division of {num1} and {num2} is {num1/num2}')
print(f'Floor division of {num1} and {num2} is {num1//num2}')
print(f'Modulus of {num1} and {num2} is {num1%num2}')
print(f'{num1} to the power of {num2} is {num1**num2}')
