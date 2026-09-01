def table(n): #->Parameter
    for i in range(1,11):
        print(f'{n}X{i}={n*i}')

table(8)#--> Argument 


# write a function to calculate area and perimeter of a rectangle

def areaNperi(length,breadth):
    area = length * breadth
    peri = 2*(length+breadth)
    print(f'The area of the rectangle with length {length} and breadth {breadth} is:{area}')
    print(f'The perimeter of the rectangle with length {length} and breadth {breadth} is: {peri}')

areaNperi(10,8)

# Write a function to find greatest among three numbers

def GreatestNum(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(f'{num1} is the greatest number among three')
    elif num2>=num3:
        print(f'{num2} is the greatest number among 3')
    else:
        print(f'{num3} is the greatest among three')

GreatestNum(10,34,4)

# write a function to find smallest number among three
def smallestNum(num1,num2,num3):
    if num1<num2 and num1<num3:
        print(f'{num1} is smallest among three')
    elif num2<num3:
        print(f'{num2} is smallest among three')
    else:
        print(f'{num3} is smallest among three')
smallestNum(1,2,3)
smallestNum(10,5,8)
'''
Output:
1 is smallest among three
5 is smallest among three
'''

# write a function to calculate discount price by passing mrp and discount
# percentage as arguments

def discountPrice(mrp,discount):
    discount_price = mrp*(discount/100)
    total_price = mrp-discount_price
    print(f'discount_price: {discount_price}')
    print(f'Total price: {total_price}')

discountPrice(1000,5)

'''
Output:
discount_price: 50.0
Total price: 950.0
'''

# write a function to calculate sum of two numbers with parameters
def sumOfNum(num1: int,num2: int) -> int:
    sum = num1 + num2
    return sum

print(sumOfNum(5,9))

# write a function to calculate age of a person
def ageCal(birYear,curYear):
    age = curYear-birYear
    return age

# print(ageCal(1987,2026))
print(f'The person will be of age {ageCal(2001,2026)+5} in 5 years')

# write two function one to calculate total of marks
#and another to calculate percentage of that total

def calculateMarks(sub1,sub2,sub3,sub4,sub5):
    total = sub1+sub2+sub3+sub4+sub5
    return total

def calculatePercentage(marks):
    percentage = (marks/500)*100
    return percentage


per = calculatePercentage(calculateMarks(67,89,60,87,50))
print(f'{per}% marks')

# write three functions one to calculate total expenses of a company
# second sales of the company
# third function which takes the above two functions as arguments and
# calculate the revenue of the company

def calculateExpenses(expenses):
    total = 0
    for exp in expenses:
        total+=exp
    return total

def calculateRevenue(revenues):
    total=0
    for rev in revenues:
        total+=rev
    return total

def profitLoss(expenses,revenues):
    total = revenues-expenses
    if revenues>expenses:
        return f'the company is running profit the total profit is: {total}'
    else:
        return f'the company is running losses the total loss is: {total}'


expenses=[20000,30000,40000,50000]
revenues = [30000,40000,10000,80000]

total_expense = calculateExpenses(expenses)
total_revenue = calculateRevenue(revenues)

print(profitLoss(total_expense,total_revenue))

'''
Output:
the company is running profit the total profit is: 20000
'''










