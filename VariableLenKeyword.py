# write a program to print names of all top 5 students in 
# a class

def toppers(**names): #names work as a dictionary
    for name in names:
        print(names[name])


toppers(topper1='manohar',topper2='varun',topper3='Kavitha'
        ,topper4='durgasri')

'''
Output:
manohar
varun
Kavitha
durgasri
'''


# write a program with variable length keyword argument
# to find sum of all the marks passed for different
# subjects

def sumOfMarks(**marks):
    totalMarks = 0
    for mark in marks:
        totalMarks+=marks[mark]
    print(f'The sum of all the subjects marks is:{totalMarks}')

sumOfMarks(maths=89,physics=78,chemistry=45,
           python=100,AI=99)



# write a program to find highest expense in a monthly
# expense of a person using variable length keyword


def highestExpense(**expenses):
    highest = 0
    total = 0
    for expense in expenses:
        if expenses[expense]>highest:
            highest=expenses[expense]
        total+=expenses[expense]
    return f'The total expense is:{total} and highest expense is: {highest}'
print(highestExpense(rent=7500,groceries=2000,
                     streetFood=2500, shopping=5000))

'''
Output:
The total expense is:17000 and
highest expense is: 7500
'''


# Write a function to display details of a person
# using tuple unpacking on the variable length parameters

def displaydetails(**details):
    print('The details are:')
    for key,value in details.items():
        print(f'{key}:{value}')


displaydetails(name='Srinivasu',quali='Msc',city='Hyderabad',phno=9988806547)


'''
Output:
name:Srinivasu
quali:Msc
city:Hyderabad
phno:9988806547
'''



# Write a function to print total bill of a restaurant by
# passing prices of the items as variable length
# argument and charges as variable length keyword arguments

def resBill(*prices,**charges):
    totalBill = 0
    for price in prices:
        totalBill +=price
    for charge in charges:
        totalBill += charges[charge]
    print(f'Total Bill: {totalBill}')

resBill(350,500,30,50,gst=40,tip=20,serCh=35)

'''
Output:
Total Bill: 1025
'''






