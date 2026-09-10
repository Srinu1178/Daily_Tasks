#ord()
print(ord('A'))
print(ord('Z'))
print(ord('a'))

# write a program to convert a charcter from uppercase to lowercase

char = input("Enter the character: ")

lower = chr(ord(char)+32)
print(lower)


# Write a function to convert a character from lower to upper

def lowerToUpper(char):
    if 'a'<=char<='z':
      upper = chr(ord(char)-32)
      return upper
    else:
       return f'Cannot convert {char} into an upper case'

print(lowerToUpper('g'))

'''
Output:
G
'''


# Input name = 'VeNkAt nArAyAnA'
# output:

# Write a function to swap case of each character in a string

def swapCase(name):
    name1 = ''
    for word in name:
        if 'a'<=word<='z':
            name1+=chr(ord(word)-32)
        elif 'A'<=word<='Z':
            name1+=chr(ord(word)+32)
        else:
            name1+=word
    return name1

print(swapCase('VeNkAt nArAyAnA'))

'''
Output:
vEnKaT NaRaYaNa
'''



# enumerate
names = ['sarath','usha sri','sumanth','srinivasu','madhesh','roshini']

for rollno, name in enumerate(names,101):
    print(f'{rollno}:{name}')

'''
Output:
101:sarath
102:usha sri
103:sumanth
104:srinivasu
105:madhesh
106:roshini
'''


# write a program to assign emp ids to each and every employee of a company 
# a function

def assignEmpIds(names):
    companyId='GDV'
    for no,name in enumerate(names,201):
        print(f'The employee {name} got emp id:{companyId+str(no)}')

assignEmpIds(['sarath','usha sri','sumanth','srinivasu','madhesh','roshini'])

'''
Output:
The employee sarath got emp id:GDV201
The employee usha sri got emp id:GDV202
The employee sumanth got emp id:GDV203
The employee srinivasu got emp id:GDV204
The employee madhesh got emp id:GDV205
The employee roshini got emp id:GDV206
'''


#zip(): 
emps = ['Bhargav','Rajesh','Kiran','Shraddha','Sunaina','Janhvi']
sals = [67000,56000,34000,87000,66000,98000]

for name,salary in zip(emps,sals):
    print(f'The employee {name} is earning a salary of {salary}')

'''
Output:
The employee Bhargav is earning a salary of 67000
The employee Rajesh is earning a salary of 56000
The employee Kiran is earning a salary of 34000
The employee Shraddha is earning a salary of 87000
The employee Sunaina is earning a salary of 66000
The employee Janhvi is earning a salary of 98000
'''


emps = ['Bhargav','Rajesh','Kiran','Shraddha','Sunaina','Janhvi']
sals = [67000,56000,34000,87000,66000,98000]
cities = ['Hyderabad','Vijayawada','Mumbai','Kolkata','Vizag','Chennai']


for name,salary,city in zip(emps,sals,cities):
    print(f'The employee {name} is earning a salary of {salary} and is from {city}')


'''
Output:
The employee Bhargav is earning a salary of 67000 and is from Hyderabad
The employee Rajesh is earning a salary of 56000 and is from Vijayawada
The employee Kiran is earning a salary of 34000 and is from Mumbai
The employee Shraddha is earning a salary of 87000 and is from Kolkata
The employee Sunaina is earning a salary of 66000 and is from Vizag
The employee Janhvi is earning a salary of 98000 and is from Chennai
'''

# # Task:
# # write a function to generate product ids for list of products also
# # combine product names with their prices and categories with zip function


def generateIds(prodName,prices,categories):
    for ids,(name,price,cat) in enumerate(zip(prodName,prices,categories,),901):
        print(f'The product id {ids} of product name {name} and price {price} in the category of {cat}')


prodName = ['laptop','earbuds','shoes','chilli powder','mobile']
prices = [69999,3000,2000,60,29999]
categories = ['Electronics','Accessories','Fashion','Groceries','Electronics']

generateIds(prodName,prices,categories)


'''
Output:
The product id 901 of product name laptop and price 69999 in the category of Electronics
The product id 902 of product name earbuds and price 3000 in the category of Accessories
The product id 903 of product name shoes and price 2000 in the category of Fashion
The product id 904 of product name chilli powder and price 60 in the category ofGroceries
The product id 905 of product name mobile and price 29999 in the category of Electronics
'''