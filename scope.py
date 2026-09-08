











#local scope
# write a function to find sum of two numbers

def sumOfNums():
    num1 = 10
    num2 = 23
    print(num1+num2)
# print(num1) # here this line gives error
sumOfNums()

'''
Output:
33
'''


# write a function to display card details of a person

def cardDetails(cardNum,pin,cvv):
    print(f'The card number is:{cardNum}')
    print(f'The pin of card is:{pin}')
    print(f'The cvv of the card is: {cvv}')

cardDetails(3455674532118956,5645,677)

# print(pin) # This line gives error

'''
Output: 
The card number is:3455674532118956
The pin of card is:5645
The cvv of the card is: 677
'''

# Write a function to withdraw money from account if balance is
# greater than withdraw amount or else print not enough balance,
# take balance as local variable withdraw as parameter.

def withdrawMoney(withdraw):
    balance = 10000
    if balance>=withdraw:
        balance-=withdraw
        print(f'withdraw successful')
        print(f'Current Balance:{balance}')
    else:
        print(f'Not enough Balance, current balance:{balance}')

money = int(input("Enter the withdraw money: "))
withdrawMoney(money)
# balance+=5000 # This line gives error

'''
Output:
Enter the withdraw money: 5800
withdraw successful
Current Balance:4200
'''


# Global Scope:
# Write two functions to calculate area and perimeter of a circle

pi = 3.14
def areaOfCir(radius):
    area = pi*radius*radius
    print(f'area of circle with radius {radius} is: {area:.2f}')

def periOfCir(radius):
    peri = 2 * pi *radius
    print(f'perimeter of the circle with radius {radius} is: {peri}')
print(f'The pi value is:{pi}')
areaOfCir(12)
periOfCir(12)


'''
Output:
The pi value is:3.14
area of circle with radius 12 is: 452.16
perimeter of the circle with radius 12 is: 75.36
'''


# Write two functions one to calculate tax of an item and another to
# calculate total price of that item by adding the tax which is calculated
# is the above function and take gst percentage as global variable

gst = 16
def taxCal(amount):
    taxAmount = amount*gst/100
    return taxAmount

def priceCal(amount):
    totalPrice = amount+taxCal(amount)
    return totalPrice

print(taxCal(59999))
print(priceCal(59999))
print(f'gst:{gst}')
'''
Output:
9599.84
69598.84
gst:16
'''

# editing a global variable in local scope
ceo = 'Tim Cook' # global Variable
def ceoAssigning():
    ceo = 'John Ternus' #local variable
    print(ceo)
ceoAssigning()
print(ceo)

'''
Output:
John Ternus
Tim Cook
'''


# Write a program to add runs to score as one function
# and displayng score as another function and take score as global
# variable

score = 0
def addScore(runs):
    global score
    score+=runs
def displayScore():
    print(score)

addScore(50)
displayScore()

'''
Output:
50
'''






