# 30 Python User Defined Function Problems
# 1. Smart Password Validator
# Concept: Function with string parameter and boolean return
# Task: Create a function validatePassword(password) that checks
# whether a password:
# Has at least 8 characters
# Contains at least one digit
# Contains at least one uppercase letter
# Example Input:
# password = 'Python123'
# Example Output:
# Valid Password

def validatePassword(password):
    has_digit = False
    has_upper = False
    for ch in password:
        if '0'<=ch<='9':
            has_digit=True
        if 'A'<=ch<'Z':
            has_upper = True
    if len(password)>=8 and has_digit and has_upper:
        return True
    else:
        return False

password = input("Enter the password: ")
if validatePassword(password):
    print("Valid Password")
else:
    print("Not valid password")

'''
Output:
Enter the password: Python123
Valid Password
'''

# 2. Digital Wallet Balance Checker
# Concept: Function with multiple parameters Task: Create a
# function checkBalance(balance, withdrawal) that returns whether
# the withdrawal is possible.
# Example Input:
# balance = 5000
# withdrawal = 3000
# Example Output:
# Transaction Approved
# Remaining Balance: 2000

def checkBalance(balance,withdrawl):
    if balance>=withdrawl:
        balance-=withdrawl
    else:
        return 'Withdraw cannot be possible'
    return f'Remaining Balance: {balance}'

balance = int(input("balance = "))
withdrawl = int(input("withdrawl = "))
print(checkBalance(balance,withdrawl))

'''
Output:
thon/Exan2/userDefinedFun.py
balance = 5000
withdrawl = 3000
Remaining Balance: 2000
'''

# 3. Temperature Converter
# Concept: Function returning calculated value Task: Create a
# function convertTemperature(celsius) to convert Celsius into
# Fahrenheit.
# Example Input:
# celsius = 35
# Example Output:
# 95 Fahrenheit

def convertTemperature(celsius):
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

cel = int(input("celsius = "))
print(f'{convertTemperature(cel)} Fahrenheit')

'''
Output:
celsius = 35
95.0 Fahrenheit
'''


# 4. Employee Bonus Calculator
# Concept: Function with conditions Task: Create a function
# calculateBonus(salary, experience):
# Experience above 5 years → 20% bonus
# Otherwise → 10% bonus
# Example Input:
# salary = 50000
# experience = 7
# Example Output:
# Bonus = 10000

def calculateBonus(salary,experience):
    if experience>5:
        return f'Bonus = {salary*0.20}'
    else:
        return f'Bonus = {salary*0.10}'
salary = int(input("salary = "))
exp = int(input('experience = '))
print(calculateBonus(salary,exp))

'''
Output:
salary = 50000
experience = 7
Bonus = 10000.0
'''

# 5. ATM Note Counter
# Concept: Function with loops Task: Create a function
# countNotes(amount) that returns the number of 500, 200, and 100
# rupee notes required.
# Example Input:
# amount = 1800
# Example Output:
# 500 notes: 3
# 200 notes: 1
# 100 notes: 1

def countNotes(amount):
    notes500 = amount//500
    amount = amount%500
    notes200 = amount//200
    amount = amount%200
    notes100 = amount//100
    amount = amount%100
    return notes500,notes200,notes100
amount = int(input("amount = "))
notes= countNotes(amount)
print(f'500 notes: {notes[0]}\n200 notes: {notes[1]}\n100 notes:{notes[2]}')

'''
Output:
amount = 1800
500 notes: 3
200 notes: 1
100 notes:1
'''

# 6. Movie Ticket Price Calculator
# Concept: Default arguments Task: Create a function
# ticketPrice(age, premium=False).
# Rules:
# Below 12 → ₹100
# Above 60 → ₹120
# Others → ₹200
# Premium adds ₹100
# Example Input:
# age = 25
# premium = True
# Example Output:
# Ticket Price: 300

def ticketPrice(age,premium=False):
    price = 0
    if age<12:
        price = 100
    elif age>60:
        price = 120
    else:
        price = 200
    if premium:
        price+=100
    return f'Ticket price: {price}'

age = int(input("Enter the age: "))
premium = input("is person plan premium true or false: ")=='true'
print(ticketPrice(age,premium))

'''
Output:
Enter the age: 25
is person plan premium true or false: true
Ticket price: 300
'''

# 7. Student Grade Generator
# Concept: Function returning grade Task: Create a function
# findGrade(marks).
# Rules:
# 90+ → A
# 75-89 → B
# 50-74 → C
# Below 50 → Fail
# Example Input:
# marks = 82
# Example Output:
# Grade B

def findGrade(marks):
    if marks>=90:
        return 'Grade A'
    elif marks>=75:
        return 'Grade B'
    elif marks>=50:
        return 'Grade C'
    else:
        return 'Fail'

marks = int(input("Enter the marks: "))
print(findGrade(marks))

'''
Output:
Enter the marks: 82
Grade B
'''

# 8. Username Generator
# Concept: String manipulation function Task: Create a function
# generateUsername(firstName, birthYear).
# Example Input:
# firstName = 'Ravi'
# birthYear = 2002
# Example Output:
# ravi2002

def generateUsername(firstName,birthYear):
    return chr(ord(firstName[0])+32)+firstName[1:]+str(birthYear)

fname = input("firstName = ")
year = int(input("birthYear = "))

print(generateUsername(fname,year))
'''
Output
firstName = Ravi
birthYear = 2002
ravi2002
'''

# 9. Electricity Usage Analyzer
# Concept: Function returning multiple values Task: Create a
# function calculateBill(units) that returns:
# Total bill
# Tax amount
# Final amount

def calculateBill(units):
    if units<=100:
        bill = units * 3
    elif units <=200:
        bill =(100*3)+(units-100)*4
    elif units <=300:
        bill =(100*3)+(100*4)+(units-200)*6
    else:
        bill = (100*3)+(100*4)+(100*6)+(units-300)*8
    tax = 5
    print(f'Total bill: {bill}')
    tax_amount = bill*(tax/100)
    print(f'Tax amount: {tax_amount}')
    f_amount = bill + tax_amount
    print(f'Final amount: {f_amount}')

units = int(input("Enter the units: "))
calculateBill(units)

'''
Output:
Enter the units: 120
Total bill: 380
Tax amount: 19.0
Final amount: 399.0
'''
    
    
# 10. Password Strength Checker
# Concept: Character checking Task: Create a function
# checkStrength(password) that returns:
# Weak
# Medium
# Strong

def checkStrength(password):
    has_digit = False
    has_upper = False
    for ch in password:
        if '0'<=ch<='9':
            has_digit = True
        if 'A'<=ch<='Z':
            has_upper=True
    if len(password)>=8 and has_upper and has_digit:
        print("Strong")
    elif len(password)>=5 and has_upper or has_digit:
        print("Medium")
    else:
        print("Weak")

passwd = input("Enter the password: ")
checkStrength(passwd)
'''
Output:
Enter the password: Python123
Strong
'''

# 11. Number Frequency Counter
# Concept: Function with list parameter Task: Create a function
# countNumber(numbers, target) that counts how many times a
# number appears.
# Example Input:
# numbers = [4,7,4,9,4]
# target = 4
# Output:
# 4 appears 3 times

def countNumber(numbers, target):
    count = 0
    for num in numbers:
        if target == num:
            count+=1
    return f'{target} appears {count} times'

numbers = [4,7,4,9,4]
target = 4
print(countNumber(numbers,target))

'''
Output:
4 appears 3 times
'''

# 12. Remove Duplicate Values
# Concept: Function returning modified list Task: Create a function
# removeDuplicates(values) without using set.
# Example Input:
# [5,2,5,8,2]
# Output:
# [5,2,8]

def removeDuplicates(values):
    i = 0
    while i<len(values)-1:
        j=i+1
        while j<len(values):
            if values[i]==values[j]:
                values.pop(j)
            else:
                j+=1
        i+=1
    return values

values = [5,2,5,8,2]
print(removeDuplicates(values))

'''
Output:
[5, 2, 8]
'''


# 13. Shopping Cart Discount
# Concept: Function with list processing Task: Create a function
# applyDiscount(prices):
# Total above 5000 gets 15% discount
# Otherwise 5%

def applyDiscount(prices):
    total = 0
    discount = 0
    for price in prices:
        total+=price
    if total>5000:
        discount=15
    else:
        discount=5
    return f'You got {discount}%, Total bill: {total-(total*(discount/100))}'

prices = [1000,1500,1300,900,600,2000]
print(applyDiscount(prices))

'''
Output:
You got 15%, Total bill: 6205.0
'''

# 14. Find Second Largest Number
# Concept: Logic inside function Task: Create a function
# secondLargest(numbers) without sorting.
# Example Input:
# [10,25,8,30]
# Output:
# 25

def secondLargest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in numbers:
        if num>largest:
            largest = num
    for num in numbers:
        if num>second_largest and num<largest:
            second_largest = num
    return second_largest

numbers = [10,25,8,30]
print(secondLargest(numbers))

'''
Output:
25
'''

# 15. Bank Loan Eligibility
# Concept: Multiple condition function Task: Create a function
# loanEligibility(income, age, creditScore).
# Return:
# Eligible
# or
# Not Eligible

def loanEligibility(income,age,creditScore):
    is_eligible = False
    if age>=21 and age<=60:
        if income>=300000 and creditScore>=700:
            is_eligible=True
    if is_eligible:
        return 'Eligible'
    else:
        return 'Not Eligible'

income = int(input("Enter your income: "))
age = int(input("Enter your age: "))
creScore = int(input("Enter the credit score: "))

print(loanEligibility(income,age,creScore))

'''
Output:
Enter your income: 300000
Enter your age: 25
Enter the credit score: 720
Eligible
'''


# 16. Email Validator
# Concept: String validation Task: Create a function
# validateEmail(email).
# Check:
# Contains @
# Contains .
# No spaces

def validateEmail(email):
    if '@' in email and '.' in email and ' ' not in email:
            return "Email is valid"
    else:
          return "Invalid email"

print(validateEmail("srinivasu@gmail.com"))

'''
Output:
Email is valid
'''

# 17. Password Generator
# Concept: Function with random logic Task: Create a function
# generatePassword(length) that creates a password of given
# length.
import random
def generatePassword(length):
    password = ''
    for i in range(length+1):
        if i>=length-1:
            password+=str(random.randint(0,9))
        else:
            password+=chr(95+random.randint(1,26))
    return password

print(generatePassword(8))

'''
Output:
pfbyw6701
'''



# 18. Delivery Charge Calculator
# Concept: Default parameter Task: Create a function
# deliveryCharge(distance, express=False).
# Rules:
# Normal: ₹10/km
# Express: ₹20/km

def deliveryCharge(distance,express=False):
    charge = 0
    if express:
        charge = distance * 20
    else:
        charge = distance * 10
    return f'The delivery charge for distance is : \u20B9{charge}'

print(deliveryCharge(10,True))

'''
Output:
The delivery charge for distance is: ₹200
'''

# 19. Library Fine Calculator
# Concept: Date logic simulation Task: Create a function
# calculateFine(daysLate).
# Rules:
# First 5 days → ₹2/day
# Next days → ₹5/day

def calculateFine(daysLate):
    fine = 0
    if daysLate<=5:
        fine = daysLate*2
    else:
        fine = (5*2)+(daysLate-5)*5
    return f'The total fine to pay: \u20B9{fine}'

print(calculateFine(8))

'''
Output:
The total fine to pay: ₹25
'''


# 20. Attendance Percentage
# Concept: Mathematical function Task: Create a function
# attendancePercentage(totalDays, presentDays).

def attendancePercentage(totalDays, presentDays):
    percent = (presentDays/totalDays)*100

    return f'The total percentage of attendence is : {percent:.2f}%'

print(attendancePercentage(180,140))

'''
Output:
The total percentage of attendence is : 77.78%
'''

# 21. Vehicle Speed Monitor
# Concept: Function returning message Task: Create a function
# checkSpeed(speed).
# Rules:
# Below 60 → Normal
# 60-100 → Warning
# Above 100 → Over Speed

def checkSpeed(speed):
    if speed<60:
        return 'Normal'
    elif speed<=100:
        return 'Warning'
    else:
        return 'Over Speed'

print(checkSpeed(60))

'''
Output:
Warning
'''

# 22. Grocery Inventory Checker
# Concept: Dictionary parameter Task: Create a function
# checkStock(items, product) that checks availability.

def checkStock(items,product):
    if product in items:
        if items[product]>0:
            print(f'Stock is available :{product}->{items[product]}')
        else:
            print(f'Out of Stock')
    else:
        print(f'The product {product} is not available in the inventory')

items={'apple':20,'banana':18,'bread':20,'milk':5}
product=input("Enter the product which one to check: ")

checkStock(items,product)

'''
Output:
Enter the product which one to check: banana
Stock is available :banana->18
'''

# 23. Word Analyzer
# Concept: String + multiple return values Task: Create a function
# analyzeWord(word) returning:
# Number of characters
# Number of vowels
# Number of consonants

def analyzeWord(word):
    vowels = 0
    cons=0
    charters = 0
    for ch in word:
        if ch in 'aeiouAEIOU':
            vowels+=1
        elif 'a'<=ch<='z' or 'A'<=ch<='Z':
            cons+=1
        elif ch!=' ':
            charters+=1
    return vowels,cons,charters

word = 'hello@ 23'
analyze = analyzeWord(word)
print(f'Vowels:{analyze[0]}')
print(f'Consonants:{analyze[1]}')
print(f'Characters: {analyze[2]}')

'''
Output:
Vowels:2
Consonants:3
Characters: 3
'''



# 24. Train Ticket Fare Calculator
# Concept: Multiple arguments Task: Create a function
# calculateFare(age, distance, classType).

def calculateFare(age,distance,classType):
    base_fare = distance * 1
    if classType.lower()=='sleeper':
        price_mul = 1
    elif classType.lower()=='3ac':
        price_mul = 2
    elif classType.lower() == '2ac':
        price_mul = 3
    elif classType.lower() == '1ac':
        price_mul=4
    else:
        price_mul=1
    fare = base_fare*price_mul

    if age<5:
        fare = 0
    elif age<12:
        fare = fare*0.5
    elif age >=60:
        fare = fare*0.4
    return f'The ticket fare is: \u20B9{fare:.2f}'

print(calculateFare(10,450,'sleeper'))

'''
Output:
The ticket fare is: ₹225.00
'''
    
# 25. Mobile Data Usage Tracker
# Concept: Function with calculations Task: Create a function
# checkDataUsage(totalData, usedData).
# Return remaining data percentage.

def checkDataUsage(totalData, usedData):
    if totalData>=usedData:
        rem = totalData - usedData
    return f'Remaining Data: {rem} MB out of {totalData} MB'

print(checkDataUsage(1000,800))

'''
Output:
Remaining Data: 200 MB out of 1000 MB
'''


# 26. Restaurant Bill Splitter
# Concept: Function with multiple outputs Task: Create a function
# splitBill(amount, people, tip).
# Return:
# Tip amount
# Final bill
# Each person's share

def splitBill(amount, people, tip):
    total = amount+tip
    eachPerson = total//people
    return f'Each person to pay the amount is: {eachPerson}'

print(splitBill(2500,4,200))

'''
Output:
Each person to pay the amount is: 675
'''


# 27. File Size Converter
# Concept: Mathematical conversion Task: Create a function
# convertSize(bytes).
# Return KB and MB.

def convertSize(bytes):
    kb = bytes/1024
    mb = bytes/(1024*1024)
    return kb,mb
conv = convertSize(1048576)

print(f'KB = {conv[0]:.2f} KB')
print(f'MB = {conv[1]:.2f} MB')

'''
Output:
KB = 1024.00 KB
MB = 1.00 MB
'''

# 28. Quiz Score Evaluator
# Concept: Function with list input Task: Create a function
# calculateScore(answers).
# Correct answer gives +1.

def calculateScore(answers):
    cor_ans = ["A","B","C"]
    score = 0
    for user_ans,corr in zip(answers,cor_ans):
        if user_ans.upper() == corr:
            score+=1
    return f'Total Score of the quiz is : {score}'

user_answers=[]
questions = {
    1:{"Q1":"which operator is used to assign the value?",
       "A":"=",
       "B":'-',
       "C":'+',
       "D":'>'},
     2:{"Q2":"which operator is used to compare the values?",
           "A":"=",
           "B":'>=',
           "C":'+',
           "D":'-'},
      3:{"Q3":"Which keyword is used to define a function ?",
               "A":"if",
               "B":'for',
               "C":'def',
               "D":'while'}
}

for key,value in questions.items():
    for option,ques in value.items():
        print(f'{option}.{value[option]}')
    answer = input("Enter your option: ")
    user_answers.append(answer)

print(calculateScore(user_answers))

'''
Output:
Q1.which operator is used to assign the value?
A.=
B.-
C.+
D.>
Enter your option: a
Q2.which operator is used to compare the values?
A.=
B.>=
C.+
D.-
Enter your option: b
Q3.Which keyword is used to define a function ?
A.if
B.for
C.def
D.while
Enter your option: d
Total Score of the quiz is : 2
'''

# 29. Employee Performance Rating
# Concept: Function with multiple conditions Task: Create a
# function performanceRating(tasksCompleted, mistakes).
# Return:
# Excellent
# Good
# Average
# Poor

def performanceRating(taskCompleted,mistakes):
    if taskCompleted>=20 and mistakes<=1:
        return 'Excellent'
    elif taskCompleted>=16 and mistakes<=3:
        return 'Good'
    elif taskCompleted>=12 and mistakes<=5:
        return 'Average'
    else:
        return 'Poor'

print(performanceRating(20,1))


'''
Output:
Excellent
'''


# 30. Smart Expense Analyzer
# Concept: Real-time function design Task: Create a function
# expenseAnalysis(expenses).
# Return:
# Total expense
# Highest expense
# Average expense
# Category with highest spending

def expenseAnalysis(expenses):
    total = 0
    count = 0
    highest = 0
    for exp in expenses:
        total+=exp
        count+=1
        if exp>highest:
            highest = exp
    avg = total/count
    return f'Total expense: {total}', f'Highest expense:{highest}',f'Average expense:{avg:.2f}'



expenses = [1000,2000,500,600,800,500,5000]

analyze = expenseAnalysis(expenses)
for data in analyze:
    print(data)


'''
Output:
Total expense: 10400
Highest expense:5000
Average expense:1485.71
'''


