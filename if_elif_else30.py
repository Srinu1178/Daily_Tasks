# Problem 1: Student Grade 
# Definition: Use if, elif, 
# and else statements to classify a student's marks into grades. 
# Task: Read the student's marks (0–100). 
# 90–100 → Grade A 75–89 → Grade B 60–74 → Grade C 35–59 → Grade D Below 35 → Fail 
# Example Input: 82
#  Example Output: Grade B 

marks = int(input("Enter the marks: "))
if marks>=90:
    print('Grade A')
elif marks>=75:
    print('Grade B')
elif marks>=60:
    print('Grade C')
elif marks>=35:
    print('Fail')

'''
Output:
Enter the marks: 82
Grade B
'''

# Problem 2: Traffic Signal Definition: Use conditional statements
#  to decide the action based on the traffic signal color. 
# Task: Read the traffic signal color.
#  Red → Stop Yelow → Get Ready Green → Go Any other color → Invalid Signal
#  Example Input: Green 
# Example Output: Go 

color = input("Enter the color of signal: ")

if color.lower()=='red':
    print("Stop")
elif color.lower()=='yellow':
    print('Get Ready Green')
elif color.lower()=='green':
    print('Go')
else:
    print("Invalid Signal")

'''
Output:
Enter the color of signal: green
Go
'''

# Problem 3: Movie Ticket Price Definition: Use conditions 
# to determine the ticket price based on age. 
# Task: Read age. Below 5 → Free 5–17 → ₹100 18–59 → ₹200 60 and above → ₹120 
# Example Input: 25 Example Output: Ticket Price: ₹200 

age = int(input("Enter the age: "))
if age<5:
    print("Ticket Price: Free")
elif age<=17:
    print("Ticket Price: ₹100")
elif age<=59:
    print("Ticket Price: ₹200")
else:
    print("Ticket Price: ₹120")

'''
Output:
Enter the age: 25
Ticket Price: ₹200
'''

# Problem 4: Electricity Bill Category Definition: 
# Use conditional statements to classify electricity usage. 
# Task: Read units consumed.
#  0–100 → Domestic 101–300 → Standard 301–500 → Premium Above 500 → Heavy User
#  Example Input: 280 Example Output: Standard 

units = int(input("Enter the consumed units: "))
if units<=100:
    print("Domestic")
elif units<=300:
    print("Standard")
elif units<=500:
    print("Premium")
else:
    print("Heavy User")

'''
Output:
Enter the consumed units: 280
Standard
'''

# Problem 5: Bank Loan Eligibility Definition: Use conditions
# to classify a customer's credit score. 
# Task: Read the credit score. 750 and above → Excelent 650–749
#  → Good 550–649 → Average Below 550 → Not Eligible 
# Example Input: 720 Example Output: Good 

credit_score = int(input("Enter the credit score: "))
if credit_score>=750:
    print("Excelent")
elif credit_score>=650:
    print("Good")
elif credit_score>=550:
    print("Average")
else:
    print("Not Eligible")

'''
Output:
Enter the credit score: 720
Good
'''

# Problem 6: BMI Category Definition:
#  Use conditions to determine BMI status. 
# Task: Read BMI value. Below 18.5 → Underweight 18.5–24.9 → 
# Normal 25–29.9 → Overweight 30 and above → Obese 
# Example Input: 27.4 Example Output: Overweight 

bmi = float(input("Enter the BMI value: "))
if bmi < 18.5:
    print("Underweight")
elif bmi <=24.90:
    print("Normal")
elif bmi <= 29.90:
    print("Overweight")
else:
    print("Obese")

'''
Output:
Enter the BMI value: 27.4
Overweight
'''

# Problem 7: Internet Speed Rating Definition: Classify internet speed
# using conditional statements. 
# Task: Read internet speed (Mbps). 
# Below 10 → Slow 10–50 → Average 51–100 → Fast Above 100 → Very Fast 
# Example Input: 75
# Example Output: Fast 

speed = int(input("Enter the speed of internet: "))

if speed<=10:
    print("Slow")
elif speed<=50:
    print("Average")
elif speed<=100:
    print("Fast")
else:
    print("Very Fast")

'''
Output:
Enter the speed of internet: 75
Fast
'''

# Problem 8: Restaurant Feedback Definition:
#  Display feedback based on the customer's rating.
#  Task: Read rating (1–5). Example Input: 5 
# Example Output: Excelent 

rating = int(input("Enter the rating: "))
if rating == 1:
    print("Worst")
elif rating == 2: 
    print("Bad")
elif rating == 3:
    print("Average")
elif rating == 4:
    print("Good")
elif rating == 5:
    print("Excelent")
else:
    print("The rating must to give between the range 1 to 5")

'''
Output:
Enter the rating: 5
Excelent
'''

# Problem 9: Cricket Score Definition: 
# Determine batting performance using runs scored. 
# Task: Read runs. 0 → Duck 1–49 →
#  Good 50–99 → Half Century 100 or more → Century
#  Example Input: 108 
# Example Output: Century 

runs = int(input("Enter the runs: "))
if runs == 0:
    print("Duck")
elif runs<=49:
    print("Good")
elif runs<=99:
    print("Half Century")
elif runs>=100:
    print("Century")

'''
Output:
Enter the runs: 108
Century
'''

# Problem 10: Attendance Status Definition: Check eligibility based on attendance
#  percentage. Task: Read attendance percentage. 
# 90–100 → Excelent 75–89 → Eligible 60–74 → Warning Below 60 → Not Eligible
#  Example Input: 78 Example Output: Eligible 

attendence = int(input("Enter the attendence percentage: "))
if attendence>=90:
    print("Excelent")
elif attendence>=75:
    print("Eligible")
elif attendence>=60:
    print("Warning")
else:
    print("Not Eligible")

'''
Output: 
Enter the attendence percentage: 78
Eligible
'''

# Problem 11: Courier Weight Charge Definition: Use conditions 
# to determine the courier category. 
# Task: Read parcel weight and display the shipping category. 
# Example Input: 8 Example Output: Medium Parcel 

weight = int(input('Enter the weight of the parcel: '))

if weight <=5:
    print("Small Parcel")
elif weight <=10:
    print("Medium Parcel")
elif weight <=20:
    print("Large Parcel")
else:
    print("Huge Parcel")

'''
Output:
Enter the weight of the parcel: 8
Medium Parcel
'''

# Problem 12: Mobile Battery Status Definition: Display 
# battery status based on battery percentage. Task: Read battery percentage. 
# Example Input: 18 Example Output: Low Battery

battery_percentage = int(input("Enter the battery percentage: "))
if battery_percentage < 10:
    print("Keep charge in mobile")
elif battery_percentage < 20:
    print("Low Battery")
elif battery_percentage < 30:
    print("Turn on Battery Saver mode")
else:
    print("Mobile charge is ok")

'''
Output:
Enter the battery percentage: 18
Low Battery
'''

# Problem 13: Air Conditioner Mode Definition: 
# Suggest the AC mode based on room temperature. 
# Task: Read room temperature. Example Input: 35 
# Example Output: Cooling Mode 

temperature = int(input("Enter the room temperature: "))

if temperature>30:
    print("Cooling mode")
elif temperature >= 25:
    print("Normal mode")
elif temperature >= 18:
    print("Eco mode/ fan mode")
else:
    print("Heating mode")

'''
Output:
Enter the room temperature: 35
Cooling mode
'''



# Problem 14: Rainfall Level Definition: Determine rainfa l intensity.
# Task: Read rainfa l in mi limeters. Example Input: 55 
# Example Output: Heavy Rain 
rainfall = float(input("Enter the rainfall intensity in mm: "))
if rainfall>=50:
    print("Heavy Rain")
elif rainfall >= 25:
    print("Moderate Rain")
elif rainfall >= 15:
    print("light Rain")
elif rainfall == 0:
    print("No Rain")
else:
    print("Invalid")

'''
Output:
Enter the rainfall intensity in mm: 55
Heavy Rain
'''


# Problem 15: Water Tank Status Definition:
#  Display the water tank status. 
# Task: Read water level percentage. 
# Example Input: 95 
# Example Output: Full

water_level_percentage = int(input("Enter the water level percentage: "))
if water_level_percentage < 0 or water_level_percentage>100:
    print("Invalid")
elif water_level_percentage>=90:
    print("Full")
elif water_level_percentage>=50:
    print("Moderate")
elif water_level_percentage>=20:
    print("Low") 
else:
    print('Very Low')

'''
Output:
Enter the water level percentage: 95
Full
'''


# Problem 16: Exam Rank Definition: Assign a class based on total marks. 
# Task: Read marks and display the class. Example Input: 88 
# Example Output: First Class 

marks = int(input("Enter the marks: "))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=80:
    print("First Class")
elif marks >= 55:
    print("Second Class")
elif marks >=35:
    print("Third class")
else:
    print("Failed")


'''
Output: 
Enter the marks: 88
First Class
'''

# Problem 17: Salary Tax Slab Definition:
#  Determine the salary tax slab. Task: Read annual salary.
#  Example Input: 850000 Example Output: Medium Tax Slab 

annual_salary = float(input("Enter the annual salary: "))
if annual_salary<=0:
    print("Invalid salary")
elif annual_salary <= 400000:
    print("Small Tax Slab")
elif annual_salary <= 1000000:
    print("Medium Tax Slab")
else:
    print("Large Tax Slab")


'''
Output:
Enter the annual salary: 850000
Medium Tax Slab
'''

# Problem 18: Hotel Room Type Definition: 
# Suggest a room based on the customer's budget.
#  Task: Read the budget. Example Input: 3500
#  Example Output: Deluxe Room 

budget = float(input("Enter the budget: "))
if budget<1000:
    print("Budget is not enough")
elif budget < 2500:
    print("Standard Room")
elif budget<5000:
    print("Deluxe Room")
elif budget<1000:
    print("Super Deluxe Room")
else:
    print("Suite")

'''
Output:
Enter the budget: 3500
Deluxe Room
'''

# Problem 19: Vehicle Speed Warning Definition:
#  Display a warning based on vehicle speed. 
# Task: Read vehicle speed. Example Input: 110 
# Example Output: Overspeed
speed = int(input("Enter the speed: "))
if speed>=80:
    print("Overspeed")
elif speed>50:
    print("Normalspeed")
elif speed>30:
    print("Ecospeed")
elif speed>0:
    print("Low speed")
else:
    print("Invalid speed")

'''
Output:
Enter the speed: 110
Overspeed
'''
#  Problem 20: Employee Performance Definition: 
# Classify employee performance. 
# Task: Read performance score.
#  Example Input: 92 
# Example Output: Outstanding 

performance = int(input("Enter the performance: "))
if performance<0 or performance>100:
    print("Invalid")
elif performance>=90:
    print("Outstanding")
elif performance>=80:
    print("Excelent")
elif performance>=70:
    print("Good")
elif performance>=50:
    print("Average")
else:
    print("Bad")

'''
Output:
Enter the performance: 92
Outstanding
'''
          

# Problem 21: Online Shopping Discount Definition: 
# Determine the discount percentage based on purchase amount. 
# Task: Read purchase amount. Example Input: 4500
# Example Output: 15% Discount

purchase_amount = int(input("Enter the purchase_amount: "))
if purchase_amount<2000:
    print("No discount")
elif purchase_amount<4000:
    print("10% Discount")
elif purchase_amount<6000:
    print("15% Discount")
elif purchase_amount<8000:
    print("20% Discount")
else:
    print("30% Discount")

'''
Output:
Enter the purchase_amount: 4500
15% Discount
'''

#  Problem 22: Data Usage Alert Definition: 
# Display internet usage status. Task: Read data usage in GB. 
# Example Input: 95 Example 
# Output: High Usage

data_usage = float(input("Enter the data usage in GB:"))
if data_usage<=0:
    print("Invalid")
elif data_usage<30:
    print("Low Usage")
elif data_usage<60:
    print("Medium Usage")
else:
    print("High Usagae")

'''
Output
Enter the data usage in GB:95
High Usagae
'''


#  Problem 23: Fuel Level Indicator Definition: 
# Display the vehicle fuel status. Task: Read fuel percentage.
#  Example Input: 12 Example Output: Low Fuel 

fuel_level = int(input("Enter the fuel level: "))
if fuel_level<0 or fuel_level>100:
    print("Invalid level")
elif fuel_level == 0:
    print("Fuel is empty")
elif fuel_level<=20:
    print("Low Fuel")
elif fuel_level<=50:
    print("Medium Fuel")
elif fuel_level <=80:
    print("Above Medium Fuel")
else:
    print("Fuel level is high")

'''
Output:
Enter the data usage in GB:95
High Usagae
'''


# Problem 24: ATM Cash Withdrawal Definition: 
# Categorize the withdrawal amount. 
# Task: Read withdrawal amount.
#  Example Input: 15000 
# Example Output: Large Withdrawal 

amount = int(input("Enter the withdrawl amount: "))
if amount <= 0:
    print("Invalid amount")
elif amount<=4000:
    print("Small Withdrawl")
elif amount <= 8000:
    print("Medium Withdrawl")
elif amount <= 12000:
    print("High Withdrawl")
else:
    print("Large Withdrawl")

'''
Output:
Enter the withdrawl amount: 15000
Large Withdrawl
'''


# Problem 25: Library Fine Definition: 
# Determine the fine category based on overdue days. 
# Task: Read overdue days. Example Input: 7 
# Example Output: Medium Fine 

due_days = int(input("Enter the due days: "))
if due_days<=0:
    print("Invalid days")
elif due_days<=5:
    print("Small Fine")
elif due_days<=10:
    print("Medium Fine")
elif due_days<=15:
    print("High Fine")
else:
    print("Huge Fine")

'''
Output:
Enter the due days: 7
Medium Fine
'''

# Problem 26: Delivery Priority Definition: Assign a delivery type
#  based on parcel weight. Task: Read parcel weight.
#  Example Input: 15
#  Example Output: Standard Delivery 

weight = int(input("Enter the weight in kgs: "))
if weight<=0:
    print("Invalid weights")
elif weight <= 10:
    print("Express Delivery")
elif weight <= 20:
    print("Standard Delivery")
else:
    print("High Delivery")

'''
Output:
Enter the weight in kgs: 15
Standard Delivery
'''

# Problem 27: Internet Data Plan Definition: Recommend a data plan.
# Task: Read monthly data usage. Example Input: 180
# Example Output: Premium Plan 

data_usage = float(input("Enter the data usage: "))
if data_usage<=0:
    print("Invalid Usage")
elif data_usage<=100:
    print("Basic Plan")
elif data_usage<=250:
    print("Standard Plan")
elif data_usage<=500:
    print("Premium Plan")
else:
    print("Unlimited Plan")

'''
Output:
Enter the data usage: 180
Standard Plan
'''

# Problem 28: Hospital Emergency Level Definition:
#  Determine emergency priority. Task: Read priority level (1–4). 
# Example Input: 2
#  Example Output: High Priority 
priority_level = int(input("Enter the level: "))
if priority_level<=0 or priority_level>4:
    print("Invalid level")
elif priority_level == 1:
    print("Very High Priority")
elif priority_level==2:
    print("High Priority")
elif priority_level==3:
    print("Medium Priority")
else:
    print("Less Priority")

'''
Output:
Enter the level: 2
High Priority
'''

# Problem 29: Hotel Star Rating Definition: 
# Display a description based on hotel rating.
#  Task: Read hotel rating (1–5). 
# Example Input: 4 
# Example Output: Very Good Hotel 

rating = int(input("Enter the rating: "))
if rating<=0 or rating>5:
    print("Invalid Rating")
elif rating==1:
    print("Bad Hotel")
elif rating==2:
    print("Medium Hotel")
elif rating==3:
    print("Good Hotel")
elif rating==4:
    print("Very Good Hotel")
else:
    print("Excelent Hotel")

'''
Output:
Enter the rating: 4
Very Good Hotel
'''

# Problem 30: E-commerce Membership Definition: Assign a membership 
# level based on yearly purchases. 
# Task: Read yearly purchase amount. 
# Example Input: 125000
# Example Output: Gold Membership 
purchase = int(input("Enter the purchase amount in a year: "))
if purchase<40000:
    print("There is no membership for you")
elif purchase <= 100000:
    print("Silver Membership")
elif purchase <= 250000:
    print("Gold Membership")
else:
    print("Premium Membership")

'''
Output:
Enter the purchase amount in a year: 125000
Gold Membership
'''