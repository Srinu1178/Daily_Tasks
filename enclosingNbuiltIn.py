# Enclosing scope 

def outer():
    prodName = 'HP Laptop'
    def inner():
        prodId = 'HP101'
        return f'The prod id of {prodName} is {prodId}'
    print(inner())

outer()

'''
Output:
The prod id of HP Laptop is HP101
'''


# write a nested function and define an enclosing variable your college
# name, and define local variable your stream of Btech and access both in
# local scope

def college():
    collegeName = 'Central University Of Andhra Pradesh'
    def stream():
        course = 'AI and DS'
        return f' I completed course {course} at {collegeName}'
    print(stream())   

college()

# non local

def college():
    collegeName = 'Central University Of Andhra Pradesh'
    def stream():
        nonlocal collegeName
        collegeName='SCIM GOVT College'
        course = 'AI and DS'
        return f'I completed course {course} at {collegeName}'
    print(collegeName)
    print(stream())
    print(collegeName)   

college()

# write a nested function to generate email ids for employee
# for a specific domain, pass domain name as parameter
# for outer function and pass emp id as parameter for inner
# function and generate the email id inside the inner function

def generateEmail(domainName):
    def empIds(empId):
        return f'{empId}@{domainName}'
    print(empIds(102))

generateEmail('gmail.com')

'''
Output:
102@gmail.com
'''

# sir tolds the program
def emailService(domain):
    def empId(empName):
        return f'{empName}@{domain}'
    return empId

domainName=emailService('microsoft.com')
empId = domainName('rasagna')
print(empId)

'''
Output:
rasagna@microsoft.com
'''

# Write a nested function to perform withdrawl in a bank. Take balance as 
# enclosing variable and withdraw as inner function and pass amount as parameter
# to the inner function and perform the withdraw if balance is greater than amount
# and also update the balance using non local keyword

def bankOperation():
    balance = 30000
    def withDrawl(withdraw):
        nonlocal balance
        if balance>=withdraw:
            balance-=withdraw
            return f'withdraw successful, remaining balance:{balance}'
        else:
            return 'insufficient funds'
    return withDrawl

bank = bankOperation()
withdraw=bank(2000)
print(withdraw)

'''
Output:
withdraw successful, remaining balance:28000
'''









