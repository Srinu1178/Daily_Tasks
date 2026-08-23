# Problem 1 Definition: Practice using Python operators in a real-world scenario.
# Task: Read food bill and GST %. Calculate GST and final bill.
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)
food_bill = float(input("Enter the food bill: "))
gst_per = float(input("Enter the gst percentage: "))

gst_bill = (food_bill * gst_per)/100
total = food_bill + gst_bill
print(f'Food Bill: {food_bill}')
print(f'GST Percentage: {gst_per}')
print(f'GST Bill: {gst_bill}')
print(f'Total Bill: {total:.2f}')

'''
Output
Enter the food bill: 855
Enter the gst percentage: 7
Food Bill: 855.0
GST Percentage: 7.0
GST Bill: 59.85
Total Bill: 914.85
'''
# Problem 2 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read mobile price and discount %. 
# Calculate discount and final price.
#  Example Input: (Sample values) Example Output: (Expected result based on input)
 
price = float(input("Enter the mobile price: "))
discount = float(input("Enter the discount percentage: "))
discount_price = price*(discount/100)
total_price = price - discount_price
print(f"Actual price of the mobile: {price:.2f}")
print(f"discount percentage: {discount}%")
print(f"discount price: {discount_price:.2f}")
print(f"Discount applied after the price of the mobile: {total_price:.2f}")

'''
Output:
Enter the mobile price: 24000
Enter the discount percentage: 20
Actual price of the mobile: 24000.00
discount percentage: 20.0%
discount price: 4800.00
Discount applied after the price of the mobile: 19200.00
'''

# Problem 3 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read liters and price/liter. Find total cost. Example Input: (Sample values)
# Example Output: (Expected result based on input) 

liters = int(input("Enter the liters: "))
price_per_liter = float(input("Enter the price per liter: "))
total_cost = liters * price_per_liter
print(f"Liters:{liters} \nprice_per_liter:{price_per_liter:.2f}")
print(f'Total cost: {total_cost:.2f}')
'''
Output:
Enter the liters: 12
Enter the price per liter: 55
Liters:12
price_per_liter:55.00
Total cost: 660.00
'''

# Problem 4 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read units and price/unit. Find bill. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input) 

units = int(input("Enter the units: "))
price_per_unit = float(input("Enter the price per unit: "))
bill = units * price_per_unit
print(f'Total Bill: {bill:.2f}')

'''
Output:
Enter the units: 8
Enter the price per unit: 56
Total Bill: 448.00
'''

# Problem 5 Definition: Practice using Python operators in a real-world scenario.
# Task: Read runs and balls. Compute (runs*100)/balls. Example Input: (Sample values)
# Example Output: (Expected result based on input) 

runs = int(input("Enter the runs: "))
balls = int(input("Enter the balls: "))

strike_rate = (runs*100)/balls
print(f'strike rate: {strike_rate:.2f}')

'''
Output:
Enter the runs: 100
Enter the balls: 35
strike rate: 285.71
'''

# Problem 6 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read marks. Check marks>=35. 
# Example Input: (Sample values) Example 
# Output: (Expected result based on input) 

marks = int(input("Enter the marks: "))
if marks>=35:
    print("passed the subject")
else:
    print("Failed the subject, Try again")

'''
Output:
Enter the marks: 60
passed the subject
'''

# Problem 7 Definition: Practice using Python operators in a real-world scenario.
# Task: Read balance and withdrawal. 
# Check balance>=withdrawal. 
# Example Input: (Sample values)
# Example Output: (Expected result based on input)

balance = int(input("Enter the balance: "))
withdrawl = int(input("Enter the amount: "))
if balance >= withdrawl:
    print(f'Withdraw of amount {withdrawl} successful, remaining balance: {balance-withdrawl}')
else:
    print("Withdraw is not possible, the balance is insufficient or withdraw amount is high")

'''
Output:
Enter the balance: 1000
Enter the amount: 560
Withdraw of amount 560 successful, remaining balance: 440
'''


#  Problem 8 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read age. Check age>=18. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input) 

age = int(input("Enter the age: "))
if age>=18:
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")

'''
Output:
Enter the age: 19
Person is eligible to vote
'''

# Problem 9 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read two passwords. Check equality.
#  Example Input: (Sample values)
#  Example Output: (Expected result based on input) 

password=input("Enter your password: ")
confirm_pass = input("Enter your confirm password: ")

if password == confirm_pass:
    print("password created sucessful")
else:
    print("Password doesn't match")

'''
Output:
Enter your password: python123
Enter your confirm password: python123
password created sucessful
'''

# Problem 10 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read order amount. Check >=500. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input)

order_amount = int(input("Enter the order amount: "))
if order_amount>=500:
    print("Free delivery")
else:
    print("Delivery charges applicable")

'''
Output:
Enter the order amount: 600 
Free delivery
'''

#  Problem 11 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read age and fitness. Eligible if age>=18 and fit. Example Input: (Sample values) 
# Example Output: (Expected result based on input) 
age = int(input("Enter the age: "))
fit = input("Are you fit: Yes or No: ")
if age>=18 and fit.lower()=="yes":
    print("The person is eligible to fit")
else:
    print("The person is not eligible to fit")

'''
Output:
Enter the age: 20
Are you fit: Yes or No: yes
The person is eligible to fit
'''

# Problem 12 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read percentage and income. Eligible if >=85 and income<300000.
# Example Input: (Sample values)
# Example Output: (Expected result based on input) 

percentage = int(input("Enter the percentage: "))
income = int(input("Enter your annual income: "))

if percentage>=85 and income <= 300000:
    print("The person eligible to scholorship")
else:
    print("The person is not eligible to scholorship")

'''
Output:
Enter the percentage: 87
Enter your annual income: 280000
The person eligible to scholorship
'''

# Problem 13 Definition: Practice using Python operators in a real-world scenario.
# Task: Read Saturday and Sunday flags. Weekend if either true.
# Example Input: (Sample values) Example Output: (Expected result based on input) 
is_saturday = input("is today saturday or not: Yes or No:  ")
is_sunday = input("is today sunday or not: Yes or No: ")

if is_saturday or is_sunday:
    print(f'Today is weekend')
else:
    print(f'Today is not weekend')


'''
Output:
is today saturday or not: Yes or No:  yes
is today sunday or not: Yes or No: no
Today is weekend
'''


# Problem 14 Definition: Practice using Python operators in a real-world scenario.
# Task: Read degree status and age. Eligible if degree and age>=21. Example Input: (Sample values)
# Example Output: (Expected result based on input)

age = int(input("Enter the age: "))
degree_status = input("Do you have degree or not: Yes or No: ")

if age>=21 and degree_status.lower()=='yes':
    print("You are graduated")
else:
    print("You are not graduated")

'''
Output:
Enter the age: 23
Do you have degree or not: Yes or No: yes
You are graduated
'''



#  Problem 15 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read current and max level. Check full. 
# Example Input: (Sample values) 
# Example Output: (Expected result based on input) 
current= int(input("Enter the current water tank level: "))
max_level = int(input("Enter the max level of tank: "))
if current == max_level:
    print("Water level is Maximum level Reached")
else:
    print("The water level is not reached maximum level")

'''
Output:
Enter the current water tank level: 5 
Enter the max level of tank: 5
Water level is Maximum level Reached
'''


# Problem 16 Definition: Practice using Python operators in a real-world scenario.
#  Task: Read hours. Cost=40*hours. Example Input: (Sample values)
#  Example Output: (Expected result based on input) 

hours = int(input("Enter the hours: "))
cost = 40 * hours
print(f"Total cost of work: {cost}")

'''
Output:
Enter the hours: 12
Total cost of work: 480
'''


# Problem 17 Definition: Practice using Python operators in a real-world scenario.
# Task: Read salary. Bonus if <50000. Example Input: (Sample values) 
# Example Output: (Expected result based on input)

salary = float(input("Enter the salary: "))
if salary < 50000:
    print("Eligible to Bonus")
else:
    print("Not eligible to Bonus")

'''
Output:
Enter the salary: 45000
Eligible to Bonus
'''

# Problem 18 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read loan and months. EMI=loan/months. Example Input: (Sample values) 
# Example Output: (Expected result based on input) 

loan = float(input("Enter the loan amount: "))
months = int(input("How many months you want to pay the amount: "))
emi = loan/months

print(f"EMI Pay Monthly: {emi:.2f}")

'''
Output:
Enter the loan amount: 200000
How many months you want to pay the amount: 12
EMI Pay Monthly: 16666.67
'''

# Problem 19 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read purchase. Cashback 5% if >2000. Example Input: (Sample values)
#  Example Output: (Expected result based on input) 

purchase = int(input("Enter the purchase amount: "))
if purchase > 2000:
    print(f'You got 5% discount, Pay amount: {purchase-(purchase*0.05):.2f}')
else:
    print(f"You pay the amount:{purchase:.2f}")

'''
Output:
Enter the purchase amount: 3000
You got 5% discount, Pay amount: 2850.00
'''


# Problem 20 Definition: Practice using Python operators in a real-world scenario. 
# Task: Read weight and height. BMI=weight/(height*height). Example Input: (Sample values)
#  Example Output: (Expected result based on input)

weight = int(input("Enter the weight: "))
height = float(input("Enter the height in meters: "))
bmi = weight/(height*height)

print(f'Body mass Index (BMI): {bmi:.2f}')

'''
Output:
Enter the weight: 60
Enter the height in meters: 1.52
Body mass Index (BMI): 25.97
'''

# Problem 21 Definition: Practice using Python operators in a real-world scenario.
#  Task: Assign same value to two vars. Check using is. Example Input: (Sample values) 
# Example Output: (Expected result based on input) 

num1 = 10
num2 = 10
if num1 is num2:
    print("Two variables pointing same reference")
else:
    print("Two variables pointing not same reference")

print(id(num1))
print(id(num2))
'''
Output: 
Two variables pointing same reference
140708999763144
140708999763144
'''
 
# Problem 22 Definition: Practice using Python operators in a real-world scenario.
#  Task: Check coupon in list using in. Example Input: (Sample values)
#  Example Output: (Expected result based on input)
coupons = [10210,20102,40101,40123,50123,45632]
coupon = int(input("Enter the coupon: "))
for i in range(len(coupons)):
    if coupon == coupons[i]:
        print(f'Found the coupon no {coupon} at index {i} in the list')
        break
else:
    print(f"Not found the coupon no {coupon}")

'''
Output:
Enter the coupon: 40101
Found the coupon no 40101 at index 2 in the list
'''


#  Problem 23 Definition: Practice using Python operators in a real-world scenario.
#  Task: Check department in tuple. Example Input: (Sample values)
#  Example Output: (Expected result based on input)

departments = ('sales','IT','Management')

dept = input("Enter the department: ").lower()
i=0
while i<len(departments):
    if  dept == departments[i].lower():
        print(f"Found the {departments[i]} department at index {i} in the tuple")
        break
    i+=1
else:
    print(f"Not Found the {dept} department at index {i} in the tuple")

'''
Output:
Enter the department: IT
Found the IT department at index 1 in the tuple
'''


#  Problem 24 Definition: Practice using Python operators in a real-world scenario. 
# Task: Use & to identify even/odd. Example Input: (Sample values)
#  Example Output: (Expected result based on input)

num = int(input("Enter the number: "))
if num&1==1:
    print(f"{num} is Odd number")
else:
    print(f"{num} is Even number")

'''
Output:
Enter the number: 31
31 is Odd number
'''

#  Problem 25 Definition: Practice using Python operators in a real-world scenario. 
# Task: Use << to double. Example Input: (Sample values)
#  Example Output: (Expected result based on input)

items = int(input("Enter the items: "))
double = items<<1
print(f'double the items: {double}')
'''
Output:
Enter the items: 100 
double the items: 200
'''

# Problem 26 Definition: Practice using Python operators in a real-world scenario. 
# Task: Use >> to halve. Example Input: (Sample values)
# Example Output: (Expected result based on input) 

items = int(input("Enter the items: "))
quarter = items>>2
print(f'quarter: {quarter}')

'''
Output:
Enter the items: 100
quarter: 25
'''

# Problem 27 Definition: Practice using Python operators in a real-world scenario. 
# Task: Use & on two permissions. Example Input: (Sample values)
# Example Output: (Expected result based on input)
read = 1<<0
write = 1<<1
execute = 1<<2

user_permission = read|write 
required_permission = read

if user_permission & required_permission:
    print("Access granted")
else:
    print("Access denied")

'''
Output:
Access granted
'''


#  Problem 28 Definition: Practice using Python operators in a real-world scenario.
#  Task: Alarm if door or motion. Example Input: (Sample values)
#  Example Output: (Expected result based on input) 

door = input("Are you open the door: yes or no: ")
motion = input("Are you moving: yes or no: ")
if door.lower()=='yes' or motion.lower()=='yes':
    print("Alarm is ringing")
else:
    print("Alarm is not ringing")

'''
Output:
Are you open the door: yes or no: yes
Are you moving: yes or no: yes
Alarm is ringing
'''

# Problem 29 Definition: Practice using Python operators in a real-world scenario. 
# Task: Eligible if attendance>=75 or project complete. Example Input: (Sample values) 
# Example Output: (Expected result based on input) Problem 

attendence = int(input("Enter the attendence percentage: "))
project = input("Have you complete the project: yes or no: ")
if attendence>=75 or project.lower()=='yes':
    print("Eligible to higher class")
else:
    print("Not eligible")

'''
Output:
Enter the attendence percentage: 78
Have you complete the project: yes or no: no
Eligible to higher class
'''

# 30 Definition: Practice using Python operators in a real-world scenario.
#  Task: Board if passport,ticket,visa all true. Example Input: (Sample values)
# Example Output: (Expected result based on input)
passport = input("Do you have passport: yes or no: ")
ticket = input("Do you have a ticket: yes or no: ")
visa = input("Do you have visa: yes or no: ")

if (passport.lower()=='yes' and ticket.lower()=='yes') and visa.lower()=='yes':
    print("Boarding approved")
else:
    print("Boarding not approved")

'''
Output:
Do you have passport: yes or no: yes
Do you have a ticket: yes or no: yes
Do you have visa: yes or no: yes
Boarding approved
'''


