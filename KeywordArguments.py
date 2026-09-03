#keyword arguments:
# These are used to pass arguments to our parameters without worring about the 
# order of parameters
# Why 
# Because here at function calling we pass the arguments assigned to the relatable
# parameters

def details(name,course,job):
    print(f'{name} has done course in {course} and currently doing the {job}')

details(job = 'Trainer',name='Venkat',course='Msc')

'''
Output:
Venkat has done course in Msc and currently doing the Trainer
'''

# Write a function to calculate and print total bill of and item based
#  on quantity along with the item name

def calculateBill(item,price,quantity):
    total_bill = quantity * price
    return f'the item purchased is {item} with payment of: {total_bill}'

print(calculateBill(price=5999,item='JBL earbuds',quantity=12))
print(calculateBill(quantity=4,item='ps5',price=67999))

'''
Output:
the item purchased is JBL earbuds with payment of: 71988
the item purchased is ps5 with payment of: 271996
'''

# write a program to calculate total electricity bill with units, price of
# each unit and fixedCharges as parameters

def electricityBill(units,price,fixedCharges):
    bill = units*price
    total_bill = bill+fixedCharges
    return f'You used {units} units at rate of {price} per unit \n \
    Your previous month bill is: {total_bill}'

print(electricityBill(price=8,units=420,fixedCharges=50))

'''
Output:
You used 420 units at rate of 8 per unit 
     Your previous month bill is: 3410
'''


# write a function to check whather a person can login into system
# based on his credentials and login time

def LoginValidation(username,password,time):
    user= 'Srinu123'
    pass1 = 'Srinu@630'
    if 10<=time<=19:
        if username == user and password == pass1:
            print("Login Successful")
        else:
            print("Invalid Credentials")
    else:
        print("Login not allowed at this time")


LoginValidation(time=12,username='Srinu123',password='Srinu@630')

'''
Output:
Login Successful
'''


# Variable length arguments
# write a function to calculate number of arguments passed to a function

def argCounter(*args):
    count = 0
    for arg in args:
        count+=1
    return f'The number of arguments passed are: {count}'
print(argCounter(1,2,3,4,5,6.7,8.9,'total'))

'''
Output:
The number of arguments passed are: 8
'''


# write a fuction with variable length arguments to calculate sum and product
# of numbers passed to it and find which is greater

def greatestNum(*args):
    sum_num = 0
    product = 1
    for ele in args:
        sum_num+=ele
        product*=ele
    if product > sum_num:
        print(f'The product {product} is greater than sum {sum_num}')
    else:
        print(f'The sum {sum_num} is greater than product {product}')

greatestNum(10,20,30,0)

'''
Output:
The product 6000 is greater than sum 60
'''


 






