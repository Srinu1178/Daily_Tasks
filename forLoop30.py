# Python Problems on for Loop
# Problem 1: Weekly Attendance
# Definition
# A for loop is used to repeat a block of code a fixed number of
# times. It is useful for processing multiple inputs one by one.
# Task
# Read the attendance (Present or Absent) of an employee for 7
# days. Count how many days the employee was present.
# Example Input
# Present
# Present
# Absent
# Present
# Absent
# Present
# Present
# Example Output
# Present Days: 5

days = 0
for week in range(1,8):
    attendence = input("Present or Absent: ")
    if attendence=='Present':
        days+=1

print(f'Present Days:{days}')

'''
Output:
Present or Absent: Present
Present or Absent: Present
Present or Absent: Absent
Present or Absent: Present
Present or Absent: Absent
Present or Absent: Present
Present or Absent: Present
Present Days:5
'''

# Problem 2: Grocery Bill
# Definition
# A for loop can be used to read multiple values and calculate their
# total.
# Task
# Read the prices of 10 grocery items. Calculate the total bill
# amount.
# Example Input
# 120
# 80
# 45
# 60
# 150
# 35
# 90
# 110
# 50
# 160
# Example Output
# Total Bill: ₹900

total_bill = 0
for item in range(1,11):
    price=int(input("Price the item: "))
    total_bill+=price
print(f'Total Bill: \u20B9{total_bill}')

'''
Output:
Price the item: 120
Price the item: 80
Price the item: 45
Price the item: 60
Price the item: 150
Price the item: 35
Price the item: 90
Price the item: 110
Price the item: 50
Price the item: 160
Total Bill: ₹900
'''

# Problem 3: Classroom Average
# Definition
# A for loop allows you to process multiple student marks and
# perform calculations.
# Task
# Read the marks of 20 students. Calculate the average marks.
# Example Input
# 50
# 60
# 70
# 80
# 90
# 40
# 55
# 65
# 75
# 85
# 60
# 70
# 80
# 90
# 50
# 60
# 70
# 80
# 90
# 100
# Example Output
# Average Marks: 71.0

total = 0
count = 0
for stu in range(1,21):
    marks = int(input(f"student {stu} marks: "))
    total+=marks
    count+=1
avg = total/count
print(f'Average: {avg}')

'''
Output:
student 1 marks: 50
student 2 marks: 60
student 3 marks: 70
student 4 marks: 80
student 5 marks: 90
student 6 marks: 40
student 7 marks: 55
student 8 marks: 65
student 9 marks: 75
student 10 marks: 85
student 11 marks: 60
student 12 marks: 70
student 13 marks: 80
student 14 marks: 90
student 15 marks: 50
student 16 marks: 60
student 17 marks: 70
student 18 marks: 80
student 19 marks: 90
student 20 marks: 100
Average: 71.0
'''


# Problem 4: Highest Temperature
# Definition
# A for loop can compare values to find the highest value.
# Task
# Read the temperatures of 7 days. Find the highest temperature.
# Example Input
# 32
# 35
# 30
# 37
# 34
# 33
# 36
# Example Output
# Highest Temperature: 37°C

highest = 0
for day in range(1,8):
    temperature = int(input(f"Enter the day {day} temperature: "))
    if temperature>highest:
        highest=temperature
print(f'Highest Temperature: {highest}\N{DEGREE SIGN}C')

'''
Output:
Enter the day 1 temperature: 32
Enter the day 2 temperature: 35
Enter the day 3 temperature: 30
Enter the day 4 temperature: 37
Enter the day 5 temperature: 34
Enter the day 6 temperature: 33
Enter the day 7 temperature: 36
Highest Temperature: 37°C
'''

# Problem 5: Lowest Salary
# Definition
# A for loop can compare values to determine the minimum value.
# Task
# Read the salaries of 15 employees. Find the lowest salary.
# Example Input
# 35000
# 42000
# 38000
# 30000
# 47000
# 52000
# 36000
# 41000
# 39000
# 45000
# 48000
# 37000
# 44000
# 50000
# 34000
# Example Output
# Lowest Salary: ₹30000

smallest = float('inf')
for emp in range(1,16):
    salary = int(input(f"Enter the {emp} employee salary: "))
    if salary<smallest:
        smallest = salary
print(f'Lowest Salary: \u20B9{smallest}')

'''
Output:
Enter the 1 employee salary: 35000
Enter the 2 employee salary: 42000
Enter the 3 employee salary: 38000
Enter the 4 employee salary: 30000
Enter the 5 employee salary: 47000
Enter the 6 employee salary: 52000
Enter the 7 employee salary: 36000
Enter the 8 employee salary: 41000
Enter the 9 employee salary: 39000
Enter the 10 employee salary: 45000
Enter the 11 employee salary: 48000
Enter the 12 employee salary: 37000
Enter the 13 employee salary: 44000
Enter the 14 employee salary: 50000
Enter the 15 employee salary: 34000
Lowest Salary: ₹30000
'''

# Problem 6: Even Seat Numbers
# Definition
# A for loop with an if statement can count values that satisfy a
# condition.
# Task
# Read 25 seat numbers. Count how many are even.
# Example Input
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# Example Output
# Even Seat Numbers: 12

even = 0
for num in range(1,26):
    seatNo = int(input("Enter the seat number: "))
    if seatNo%2==0:
        even+=1
print(f'Even Seat Numbers: {even}')

'''
Output:
Enter the seat number: 11
Enter the seat number: 12
Enter the seat number: 13
Enter the seat number: 14
Enter the seat number: 15
Enter the seat number: 16
Enter the seat number: 17
Enter the seat number: 18
Enter the seat number: 19
Enter the seat number: 20
Enter the seat number: 21
Enter the seat number: 22
Enter the seat number: 23
Enter the seat number: 24
Enter the seat number: 25
Enter the seat number: 26
Enter the seat number: 27
Enter the seat number: 28
Enter the seat number: 29
Enter the seat number: 30
Enter the seat number: 31
Enter the seat number: 32
Enter the seat number: 33
Enter the seat number: 34
Enter the seat number: 35
Even Seat Numbers: 12
'''

# Problem 7: Cricket Runs
# Definition
# A for loop can repeatedly add values to calculate a total.
# Task
# Read the runs scored in 10 matches. Find the total runs.
# Example Input
# 45
# 60
# 35
# 80
# 55
# 40
# 90
# 75
# 65
# 50
# Example Output
# Total Runs: 595
total_runs = 0
for match in range(1,11):
    runs = int(input(f"Enter the runs in {match} match:"))
    total_runs+=runs
print(f'Total Runs: {total_runs}')

'''
Output:
Enter the runs in 1 match:45
Enter the runs in 2 match:60
Enter the runs in 3 match:35
Enter the runs in 4 match:80
Enter the runs in 5 match:55
Enter the runs in 6 match:40
Enter the runs in 7 match:90
Enter the runs in 8 match:75
Enter the runs in 9 match:65
Enter the runs in 10 match:50
Total Runs: 595
'''

# Problem 8: Bus Passengers
# Definition
# A for loop is useful for processing repeated daily or stop-wise
# data.
# Task
# Read the number of passengers entering the bus at 8 stops. Find
# the total passengers.
# Example Input
# 10
# 8
# 12
# 15
# 9
# 7
# 14
# 11
# Example Output
# Total Passengers: 86

total = 0
for stop in range(1,9):
    passengers = int(input(f"Enter the number of passengers at bus stop {stop}: "))
    total += passengers

print(f'Total Passengers: {total}')

'''
Output:
Enter the number of passengers at bus stop 1: 10
Enter the number of passengers at bus stop 2: 8
Enter the number of passengers at bus stop 3: 12
Enter the number of passengers at bus stop 4: 15
Enter the number of passengers at bus stop 5: 9
Enter the number of passengers at bus stop 6: 7
Enter the number of passengers at bus stop 7: 14
Enter the number of passengers at bus stop 8: 11
Total Passengers: 86
'''


# Problem 9: Mobile Recharge
# Definition
# A for loop with an if statement can count values that meet a
# condition.
# Task
# Read the recharge amount of 12 customers. Count how many
# customers recharged more than ₹500.
# Example Input
# 199
# 299
# 599
# 799
# 450
# 650
# 500
# 550
# 899
# 250
# 700
# 350
# Example Output
# Customers Above ₹500: 6

count = 0
for cus in range(1,13):
    recharge = int(input(f"Enter the amount of customer {cus}: "))
    if recharge>500:
        count+=1
print(f'Customers Above \u20B9500: {count}')

'''
Output:
Enter the amount of customer 1: 199
Enter the amount of customer 2: 299
Enter the amount of customer 3: 599
Enter the amount of customer 4: 799
Enter the amount of customer 5: 450
Enter the amount of customer 6: 650
Enter the amount of customer 7: 500
Enter the amount of customer 8: 550
Enter the amount of customer 9: 899   
Enter the amount of customer 10: 250
Enter the amount of customer 11: 700
Enter the amount of customer 12: 350
Customers Above ₹500: 6
'''

# Problem 10: Online Orders
# Definition
# A for loop is commonly used to analyze repeated business
# records.
# Task
# Read the value of 20 online orders. Count how many orders are
# above ₹1000.
# Example Input
# 1200
# 950
# 1800
# 600
# 1500
# 800
# 2100
# 1000
# 1300
# 700
# 1600
# 500
# 1100
# 900
# 1400
# 1050
# 650
# 1750
# 980
# 1250
# Example Output
# Orders Above ₹1000: 11

count = 0
for ord in range(1,21):
    price = int(input(f"Enter the value of order {ord}: "))
    if price>1000:
        count+=1
print(f'Orders Above \u20B91000: {count}')

'''
Output:
Enter the value of order 1: 1200
Enter the value of order 2: 950
Enter the value of order 3: 1800
Enter the value of order 4: 600
Enter the value of order 5: 1500
Enter the value of order 6: 800
Enter the value of order 7: 2100
Enter the value of order 8: 1000
Enter the value of order 9: 1300
Enter the value of order 10: 700
Enter the value of order 11: 1600
Enter the value of order 12: 500
Enter the value of order 13: 1100
Enter the value of order 14: 900
Enter the value of order 15: 1400
Enter the value of order 16: 1050
Enter the value of order 17: 650
Enter the value of order 18: 1750
Enter the value of order 19: 980
Enter the value of order 20: 1250
Orders Above ₹1000: 11
'''

# Problem 11: Water Bottles
# Definition
# A for loop can be used to compare values repeatedly and find the
# smallest value.
# Task
# Read the capacity (in ml) of 15 water bottles. Find the smallest
# bottle capacity.
# Example Input
# 1000
# 750
# 500
# 1500
# 2000
# 650
# 900
# 800
# 1200
# 700
# 950
# 600
# 1100
# 1300
# 550
# Example Output
# Smallest Capacity: 500 ml

smallest = float('inf')
for bottle in range(1,16):
    capacity = int(input(f"Enter the capacity of bottle(ml){bottle}:"))
    if capacity<smallest:
        smallest=capacity
print(f'smallest capacity: {smallest} ml')
    
'''
Output:
Enter the capacity of bottle(ml)1:1000
Enter the capacity of bottle(ml)2:750
Enter the capacity of bottle(ml)3:500
Enter the capacity of bottle(ml)4:1500
Enter the capacity of bottle(ml)5:2000
Enter the capacity of bottle(ml)6:650
Enter the capacity of bottle(ml)7:900
Enter the capacity of bottle(ml)8:800
Enter the capacity of bottle(ml)9:1200
Enter the capacity of bottle(ml)10:700
Enter the capacity of bottle(ml)11:950
Enter the capacity of bottle(ml)12:600
Enter the capacity of bottle(ml)13:1100
Enter the capacity of bottle(ml)14:1300
Enter the capacity of bottle(ml)15:550
Smallest Capacity: 500 ml
'''

# Problem 12: Electricity Consumption
# Definition
# A for loop can process multiple values and calculate their total.
# Task
# Read the electricity units consumed by 10 houses. Find the total
# units consumed.
# Example Input
# 120
# 140
# 95
# 160
# 180
# 110
# 130
# 150
# 100
# 170
# Example Output
# Total Units Consumed: 1355

total = 0
for house in range(1,11):
    units = int(input(f"Enter the units consumed in house {house}: "))
    total +=units
print(f'Total Units Consumed: {total}')

'''
Output:
Enter the units consumed in house 1: 120
Enter the units consumed in house 2: 140
Enter the units consumed in house 3: 95
Enter the units consumed in house 4: 160
Enter the units consumed in house 5: 180
Enter the units consumed in house 6: 110
Enter the units consumed in house 7: 130
Enter the units consumed in house 8: 150
Enter the units consumed in house 9: 100
Enter the units consumed in house 10: 170
Total Units Consumed: 1355
'''


# Problem 13: Exam Pass Count
# Definition
# A for loop combined with an if statement can count values that
# satisfy a condition.
# Task
# Read the marks of 30 students. Count how many students
# passed (marks ≥ 35).
# Example Input
# 45
# 60
# 22
# 70
# 81
# 34
# 56
# 90
# 40
# 18
# 35
# 67
# 72
# 30
# 55
# 39
# 84
# 92
# 25
# 41
# 37
# 28
# 65
# 76
# 88
# 31
# 58
# 69
# 47
# 80
# Example Output
# Students Passed: 23

count = 0
for student in range(1,31):
    marks = int(input(f"Enter the student {student} marks: "))
    if marks>=35:
        count+=1

print(f'Students Passed: {count}')

'''
Output:
Enter the student 1 marks: 45
Enter the student 2 marks: 60
Enter the student 3 marks: 22
Enter the student 4 marks: 70
Enter the student 5 marks: 81
Enter the student 6 marks: 34
Enter the student 7 marks: 56
Enter the student 8 marks: 90
Enter the student 9 marks: 40
Enter the student 10 marks: 18
Enter the student 11 marks: 35
Enter the student 12 marks: 67
Enter the student 13 marks: 72
Enter the student 14 marks: 30
Enter the student 15 marks: 55
Enter the student 16 marks: 39
Enter the student 17 marks: 84
Enter the student 18 marks: 92
Enter the student 19 marks: 25
Enter the student 20 marks: 41
Enter the student 21 marks: 37
Enter the student 22 marks: 28
Enter the student 23 marks: 65
Enter the student 24 marks: 76
Enter the student 25 marks: 88
Enter the student 26 marks: 31
Enter the student 27 marks: 58
Enter the student 28 marks: 69
Enter the student 29 marks: 47
Enter the student 30 marks: 80
Students Passed: 23
'''

# Problem 14: Rainfall Record
# Definition
# A for loop can compare values to determine the highest value.
# Task
# Read the rainfall (in mm) for 12 months. Find the month with the
# highest rainfall.
# Example Input
# 120
# 145
# 98
# 175
# 162
# 110
# 90
# 135
# 155
# 180
# 170
# 140
# Example Output
# Highest Rainfall: 180 mm
# Month Number: 10

highest = 0
monthNum = 0
for month in range(1,13):
    rain = int(input("Enter the rainfall (in mm): "))
    if rain>highest:
        highest = rain
        monthNum = month
print(f'Highest Rainfall: {highest} mm')
print(f'Month Number: {monthNum}')

'''
Output:
Enter the rainfall (in mm): 175
Enter the rainfall (in mm): 162
Enter the rainfall (in mm): 110
Enter the rainfall (in mm): 90
Enter the rainfall (in mm): 135
Enter the rainfall (in mm): 155
Enter the rainfall (in mm): 180
Enter the rainfall (in mm): 170
Enter the rainfall (in mm): 140
Highest Rainfall: 180 mm
Month Number: 10
'''


# Problem 15: Hospital Patients
# Definition
# A for loop with an if statement helps count records matching a
# condition.
# Task
# Read the ages of 20 patients. Count how many are senior citizens
# (age ≥ 60).
# Example Input
# 45
# 62
# 58
# 70
# 39
# 65
# 81
# 50
# 61
# 47
# 73
# 55
# 66
# 29
# 60
# 68
# 42
# 75
# 59
# 64
# Example Output
# Senior Citizens: 11

seniors = 0
for patient in range(1,21):
    age = int(input(f"Enter the age of patient {patient}: "))
    if age>=60:
        seniors+=1

print(f'Senior Citizens: {seniors}')

'''
Output:
Enter the age of patient 1: 45
Enter the age of patient 2: 62
Enter the age of patient 3: 58
Enter the age of patient 4: 70
Enter the age of patient 5: 39
Enter the age of patient 6: 65
Enter the age of patient 7: 81
Enter the age of patient 8: 50
Enter the age of patient 9: 61
Enter the age of patient 10: 47
Enter the age of patient 11: 73
Enter the age of patient 12: 55
Enter the age of patient 13: 66
Enter the age of patient 14: 29
Enter the age of patient 15: 60
Enter the age of patient 16: 68
Enter the age of patient 17: 42
Enter the age of patient 18: 75
Enter the age of patient 19: 59
Enter the age of patient 20: 64
Senior Citizens: 11
'''

# Problem 16: Library Books
# Definition
# A for loop can compare values to find the maximum value.
# Task
# Read the number of pages in 10 books. Find the book with the
# maximum pages.
# Example Input
# 250
# 320
# 180
# 410
# 290
# 375
# 460
# 340
# 280
# 390
# Example Output
# Maximum Pages: 460

maximum = 0
for book in range(1,11):
    pages = int(input(f"Number of pages in book {book}: "))
    if pages>maximum:
        maximum = pages
print(f'Maximum pages: {maximum}')

'''
Output:
Number of pages in book 1: 250
Number of pages in book 2: 320
Number of pages in book 3: 180
Number of pages in book 4: 410
Number of pages in book 5: 290
Number of pages in book 6: 375
Number of pages in book 7: 460
Number of pages in book 8: 340
Number of pages in book 9: 280
Number of pages in book 10: 390
Maximum pages: 460
'''

# Problem 17: Bike Mileage
# Definition
# A for loop can calculate totals and averages from multiple inputs.
# Task
# Read the mileage (km/l) of 15 bikes. Calculate the average
# mileage.
# Example Input
# 45
# 50
# 55
# 48
# 60
# 52
# 47
# 58
# 53
# 49
# 57
# 51
# 54
# 56
# 50
# Example Output
# Average Mileage: 52.3 km/l

total = 0
count = 0
for bike in range(1,16):
    mileage = int(input(f"Enter the mileage of bike {bike}: "))
    total+=mileage
    count+=1
avg = total/count
print(f"Average Mileage: {avg:.1f} km/l")

'''
Output:
Enter the mileage of bike 1: 45
Enter the mileage of bike 2: 50
Enter the mileage of bike 3: 55
Enter the mileage of bike 4: 48
Enter the mileage of bike 5: 60
Enter the mileage of bike 6: 52
Enter the mileage of bike 7: 47
Enter the mileage of bike 8: 58
Enter the mileage of bike 9: 53
Enter the mileage of bike 10: 49
Enter the mileage of bike 11: 57
Enter the mileage of bike 12: 51
Enter the mileage of bike 13: 54
Enter the mileage of bike 14: 56
Enter the mileage of bike 15: 50
Average Mileage: 52.3 km/l
'''

# Problem 18: Employee Bonus
# Definition
# A for loop with an if statement can count employees who satisfy
# a condition.
# Task
# Read the salaries of 20 employees. Count how many employees
# are eligible for a bonus (salary < ₹50000).
# Example Input
# 45000
# 52000
# 38000
# 61000
# 47000
# 55000
# 49000
# 68000
# 43000
# 51000
# 36000
# 59000
# 48000
# 62000
# 41000
# 53000
# 39000
# 57000
# 46000
# 65000
# Example Output
# Employees Eligible for Bonus: 10

count = 0
for emp in range(1,21):
    salary = int(input(f"Enter the salary of employee {emp}: "))
    if salary<50000:
        count+=1
print(f'Employee Eligible for Bonus: {count}')

'''
Output:
Enter the salary of employee 1: 45000
Enter the salary of employee 2: 52000
Enter the salary of employee 3: 38000
Enter the salary of employee 4: 61000
Enter the salary of employee 5: 47000
Enter the salary of employee 6: 55000
Enter the salary of employee 7: 49000
Enter the salary of employee 8: 68000
Enter the salary of employee 9: 43000
Enter the salary of employee 10: 51000
Enter the salary of employee 11: 36000
Enter the salary of employee 12: 59000
Enter the salary of employee 13: 48000
Enter the salary of employee 14: 62000
Enter the salary of employee 15: 41000
Enter the salary of employee 16: 53000
Enter the salary of employee 17: 39000
Enter the salary of employee 18: 57000
Enter the salary of employee 19: 46000
Enter the salary of employee 20: 65000
Employee Eligible for Bonus: 10
'''


# Problem 19: Fuel Filling Station
# Definition
# A for loop is useful for calculating totals from repeated entries.
# Task
# Read the liters of fuel filled by 10 customers. Find the total liters
# sold.
# Example Input
# 15
# 20
# 18
# 25
# 12
# 30
# 16
# 22
# 14
# 28
# Example Output
# Total Fuel Sold: 200 Liters

total = 0
for customer in range(1,11):
    fuel = int(input(f"Enter the liters of fuel in customer {customer}: "))
    total+=fuel
print(f'Total Fuel Sold: {total} Liters')

'''
Output:
Enter the liters of fuel in customer 1: 15
Enter the liters of fuel in customer 2: 20
Enter the liters of fuel in customer 3: 18
Enter the liters of fuel in customer 4: 25
Enter the liters of fuel in customer 5: 12
Enter the liters of fuel in customer 6: 30
Enter the liters of fuel in customer 7: 16
Enter the liters of fuel in customer 8: 22
Enter the liters of fuel in customer 9: 14
Enter the liters of fuel in customer 10: 28
Total Fuel Sold: 200 Liters
'''

# Problem 20: Product Ratings
# Definition: A for loop and an if statement can count values that match a
# specific condition.
# Task: Read the ratings (1–5) of 25 products. Count how many products
# received a rating of 5.
# Example Input
# 5
# 4
# 3
# 5
# 2
# 5
# 1
# 4
# 5
# 3
# 5
# 2
# 4
# 5
# 1
# 5
# 3
# 4
# 5
# 2
# 5
# 4
# 3
# 5
# 5
# Example Output
# Products Rated 5 Stars: 11

count = 0
for prod in range(1,26):
    ratings = int(input(f"Enter the rating(1-5) in product {prod}: "))
    if ratings == 5:
        count+=1
print(f'Products Rated 5 Stars: {count}')

'''
Output:
Enter the rating(1-5) in product 1: 5
Enter the rating(1-5) in product 2: 4
Enter the rating(1-5) in product 3: 3
Enter the rating(1-5) in product 4: 5
Enter the rating(1-5) in product 5: 2
Enter the rating(1-5) in product 6: 5
Enter the rating(1-5) in product 7: 1
Enter the rating(1-5) in product 8: 4 
Enter the rating(1-5) in product 9: 5
Enter the rating(1-5) in product 10: 3
Enter the rating(1-5) in product 11: 5
Enter the rating(1-5) in product 12: 2
Enter the rating(1-5) in product 13: 4
Enter the rating(1-5) in product 14: 5
Enter the rating(1-5) in product 15: 1
Enter the rating(1-5) in product 16: 5
Enter the rating(1-5) in product 17: 3
Enter the rating(1-5) in product 18: 4
Enter the rating(1-5) in product 19: 5
Enter the rating(1-5) in product 20: 2
Enter the rating(1-5) in product 21: 5
Enter the rating(1-5) in product 22: 4
Enter the rating(1-5) in product 23: 3
Enter the rating(1-5) in product 24: 5
Enter the rating(1-5) in product 25: 5
Products Rated 5 Stars: 11
'''


# Problem 21: Hotel Room Rent
# Definition: A for loop can be used to compare multiple values and find the
# highest value.
# Task: Read the room rent of 12 hotel bookings. Find the highest room
# rent.
# Example Input
# 2500
# 3200
# 2800
# 4500
# 3900
# 5100
# 4700
# 3600
# 4200
# 3800
# 4900
# 5300
# Example Output
# Highest Room Rent: ₹5300

highest = 0
for hotel in range(1,13):
    rent = int(input(f"Enter the room rent of hotel {hotel}: "))
    if rent>highest:
        highest = rent
print(f'Highest Room Rent: \u20B9{highest}')

'''
Output:
Enter the room rent of hotel 1: 2500
Enter the room rent of hotel 2: 3200
Enter the room rent of hotel 3: 2800
Enter the room rent of hotel 4: 4500
Enter the room rent of hotel 5: 3900
Enter the room rent of hotel 6: 5100
Enter the room rent of hotel 7: 4700
Enter the room rent of hotel 8: 3600
Enter the room rent of hotel 9: 4200
Enter the room rent of hotel 10: 3800
Enter the room rent of hotel 11: 4900
Enter the room rent of hotel 12: 5300
Highest Room Rent: ₹5300
'''


# Problem 22: ATM Transactions
# Definition
# A for loop with an if statement can count values that satisfy a
# condition.
# Task
# Read the withdrawal amounts of 15 customers. Count how many
# customers withdrew more than ₹10000.
# Example Input
# 5000
# 12000
# 8000
# 15000
# 20000
# 9500
# 11000
# 7500
# 18000
# 6000
# 13000
# 4000
# 9000
# 25000
# 7000
# Example Output
# Customers Withdrawing More Than ₹10000: 7

count = 0
for cust in range(1,16):
    amount = int(input(f"Enter the withdraw amount of customer {cust}: "))
    if amount>10000:
        count+=1
print(f'Customers Withdrawing More Than \u20B910000: {count}')

'''
Output:
Enter the withdraw amount of customer 1: 5000
Enter the withdraw amount of customer 2: 12000
Enter the withdraw amount of customer 3: 8000
Enter the withdraw amount of customer 4: 15000
Enter the withdraw amount of customer 5: 20000
Enter the withdraw amount of customer 6: 9500
Enter the withdraw amount of customer 7: 11000
Enter the withdraw amount of customer 8: 7500
Enter the withdraw amount of customer 9: 18000
Enter the withdraw amount of customer 10: 6000
Enter the withdraw amount of customer 11: 13000
Enter the withdraw amount of customer 12: 4000
Enter the withdraw amount of customer 13: 9000
Enter the withdraw amount of customer 14: 25000
Enter the withdraw amount of customer 15: 7000
Customers Withdrawing More Than ₹10000: 7
'''

# Problem 23: Internet Data Usage
# Definition: A for loop is useful for repeatedly reading values and calculating
# totals.
# Task: Read the daily internet usage (GB) for 30 days. Find the total data
# used.
# Example Input
# 2
# 3
# 2
# 4
# 5
# 3
# 2
# 4
# 3
# 2
# 5
# 4
# 3
# 2
# 3
# 4
# 5
# 2
# 3
# 4
# 2
# 3
# 5
# 4
# 3
# 2
# 4
# 3
# 2
# 5
# Example Output
# Total Data Used: 98 GB

data = 0
for day in range(1,31):
    usage = int(input(f"Enter the usage of data in day {day}: "))
    data+=usage
print(f'Total Data Used: {data} GB')

'''
Output:
Enter the usage of data in day 1: 2
Enter the usage of data in day 2: 3
Enter the usage of data in day 3: 2
Enter the usage of data in day 4: 4
Enter the usage of data in day 5: 5
Enter the usage of data in day 6: 3
Enter the usage of data in day 7: 2
Enter the usage of data in day 8: 4
Enter the usage of data in day 9: 3
Enter the usage of data in day 10: 2
Enter the usage of data in day 11: 5
Enter the usage of data in day 12: 4
Enter the usage of data in day 13: 3
Enter the usage of data in day 14: 2
Enter the usage of data in day 15: 3
Enter the usage of data in day 16: 4
Enter the usage of data in day 17: 5
Enter the usage of data in day 18: 2
Enter the usage of data in day 19: 3
Enter the usage of data in day 20: 4
Enter the usage of data in day 21: 2
Enter the usage of data in day 22: 3
Enter the usage of data in day 23: 5
Enter the usage of data in day 24: 4
Enter the usage of data in day 25: 3
Enter the usage of data in day 26: 2
Enter the usage of data in day 27: 4
Enter the usage of data in day 28: 3
Enter the usage of data in day 29: 2
Enter the usage of data in day 30: 5
Total Data Used: 98 GB
'''

# Problem 24: Car Speeds
# Definition
# A for loop combined with an if statement can count values
# matching a condition.
# Task
# Read the speeds of 20 cars. Count how many cars exceeded 80
# km/h.
# Example Input
# 75
# 82
# 68
# 95
# 78
# 84
# 90
# 65
# 88
# 76
# 81
# 92
# 70
# 79
# 85
# 87
# 72
# 83
# 91
# 77
# Example Output
# Cars Above 80 km/h: 11

count = 0
for car in range(1,21):
    speed = int(input(f"Enter the car {car} speed: "))
    if speed>80:
        count+=1
print(f'Cars Above 80 km/h: {count}')

'''
Output:
Enter the car 1 speed: 75
Enter the car 2 speed: 82
Enter the car 3 speed: 68
Enter the car 4 speed: 95
Enter the car 5 speed: 78
Enter the car 6 speed: 84
Enter the car 7 speed: 90
Enter the car 8 speed: 65
Enter the car 9 speed: 88
Enter the car 10 speed: 76
Enter the car 11 speed: 81
Enter the car 12 speed: 92
Enter the car 13 speed: 70
Enter the car 14 speed: 79
Enter the car 15 speed: 85
Enter the car 16 speed: 87
Enter the car 17 speed: 72
Enter the car 18 speed: 83
Enter the car 19 speed: 91
Enter the car 20 speed: 77
Cars Above 80 km/h: 11
'''

# Problem 25: Cinema Tickets
# Definition
# A for loop can calculate the total of multiple values.
# Task
# Read the ticket prices of 30 customers. Find the total ticket
# collection.
# Example Input
# 150
# 200
# 180
# 150
# 220
# 180
# 200
# 150
# 180
# 200
# 150
# 220
# 180
# 200
# 150
# 180
# 220
# 150
# 200
# 180
# 150
# 220
# 180
# 200
# 150
# 180
# 220
# 150
# 200
# 180
# Example Output
# Total Ticket Collection: ₹5470

total = 0
for cust in range(1,31):
    ticket = int(input(f"Enter the price of ticket for customer {cust}:"))
    total+=ticket
print(f'Total Ticket Collection: \u20B9{total}')

'''
Output:
Enter the price of ticket for customer 1:150
Enter the price of ticket for customer 2:200
Enter the price of ticket for customer 3:180
Enter the price of ticket for customer 4:150
Enter the price of ticket for customer 5:220
Enter the price of ticket for customer 6:180
Enter the price of ticket for customer 7:200
Enter the price of ticket for customer 8:150
Enter the price of ticket for customer 9:180
Enter the price of ticket for customer 10:200
Enter the price of ticket for customer 11:150
Enter the price of ticket for customer 12:220
Enter the price of ticket for customer 13:180
Enter the price of ticket for customer 14:200
Enter the price of ticket for customer 15:150
Enter the price of ticket for customer 16:180
Enter the price of ticket for customer 17:220
Enter the price of ticket for customer 18:150
Enter the price of ticket for customer 19:200
Enter the price of ticket for customer 20:180
Enter the price of ticket for customer 21:150
Enter the price of ticket for customer 22:220
Enter the price of ticket for customer 23:180
Enter the price of ticket for customer 24:200
Enter the price of ticket for customer 25:150
Enter the price of ticket for customer 26:180
Enter the price of ticket for customer 27:220
Enter the price of ticket for customer 28:150
Enter the price of ticket for customer 29:200
Enter the price of ticket for customer 30:180
Total Ticket Collection: ₹5470
'''

# Problem 26: Warehouse Boxes
# Definition
# A for loop can compare values to determine the largest value.
# Task
# Read the weight of 20 boxes. Find the heaviest box.
# Example Input
# 25
# 18
# 32
# 27
# 40
# 35
# 22
# 38
# 30
# 28
# 45
# 26
# 31
# 36
# 29
# 41
# 24
# 39
# 33
# 37
# Example Output
# Heaviest Box: 45 kg

heavy = 0
for box in range(1,21):
    weight = int(input(f"Enter the weight of box {box} in kgs: "))
    if weight>heavy:
        heavy = weight
print(f'Heaviest Box: {heavy} kg')

'''
Output:
Enter the weight of box 1 in kgs: 25
Enter the weight of box 2 in kgs: 18
Enter the weight of box 3 in kgs: 32
Enter the weight of box 4 in kgs: 27
Enter the weight of box 5 in kgs: 40
Enter the weight of box 6 in kgs: 35
Enter the weight of box 7 in kgs: 22
Enter the weight of box 8 in kgs: 38
Enter the weight of box 9 in kgs: 30
Enter the weight of box 10 in kgs: 28
Enter the weight of box 11 in kgs: 45
Enter the weight of box 12 in kgs: 26
Enter the weight of box 13 in kgs: 31
Enter the weight of box 14 in kgs: 36
Enter the weight of box 15 in kgs: 29
Enter the weight of box 16 in kgs: 41
Enter the weight of box 17 in kgs: 24
Enter the weight of box 18 in kgs: 39
Enter the weight of box 19 in kgs: 33
Enter the weight of box 20 in kgs: 37
Heaviest Box: 45 kg
'''

# Problem 27: Phone Battery Levels
# Definition
# A for loop and an if statement can count values that satisfy a
# condition.
# Task
# Read the battery percentage of 15 phones. Count how many
# phones have a battery level below 20%.
# Example Input
# 18
# 45
# 12
# 67
# 9
# 80
# 25
# 15
# 32
# 5
# 90
# 17
# 50
# 14
# 60
# Example Output
# Phones Below 20% Battery: 7

count = 0
for phone in range(1,16):
    battery = int(input(f"Enter the percentage of battery in phone {phone}: "))
    if battery<20:
        count+=1
print(f'Phones Below 20% Battery: {count}')

'''
Output:
Enter the percentage of battery in phone 1: 18
Enter the percentage of battery in phone 2: 45
Enter the percentage of battery in phone 3: 12
Enter the percentage of battery in phone 4: 67
Enter the percentage of battery in phone 5: 9
Enter the percentage of battery in phone 6: 80
Enter the percentage of battery in phone 7: 25
Enter the percentage of battery in phone 8: 15
Enter the percentage of battery in phone 9: 32
Enter the percentage of battery in phone 10: 5
Enter the percentage of battery in phone 11: 90
Enter the percentage of battery in phone 12: 17
Enter the percentage of battery in phone 13: 50
Enter the percentage of battery in phone 14: 14
Enter the percentage of battery in phone 15: 60
Phones Below 20% Battery: 7
'''

# Problem 28: Daily Expenses
# Definition
# A for loop can repeatedly read values and calculate a total.
# Task
# Read the daily expenses for 30 days. Find the total monthly
# expense.
# Example Input
# 250
# 300
# 280
# 320
# 275
# 310
# 295
# 260
# 340
# 315
# 290
# 305
# 285
# 325
# 300
# 295
# 310
# 275
# 330
# 290
# 300
# 310
# 280
# 295
# 315
# 305
# 290
# 320
# 300
# 310
# Example Output
# Total Monthly Expense: ₹8975

total = 0
for day in range(1,31):
    expense = int(input(f"Enter the expenses in day {day}: "))
    total+=expense

print(f'Total Monthly Expense: \u20B9{total}')

'''
Output:
Enter the expenses in day 1: 250
Enter the expenses in day 2: 300
Enter the expenses in day 3: 280
Enter the expenses in day 4: 320
Enter the expenses in day 5: 275
Enter the expenses in day 6: 310
Enter the expenses in day 7: 295
Enter the expenses in day 8: 260
Enter the expenses in day 9: 340
Enter the expenses in day 10: 315
Enter the expenses in day 11: 290
Enter the expenses in day 12: 305
Enter the expenses in day 13: 285
Enter the expenses in day 14: 325
Enter the expenses in day 15: 300
Enter the expenses in day 16: 295
Enter the expenses in day 17: 310
Enter the expenses in day 18: 275
Enter the expenses in day 19: 330
Enter the expenses in day 20: 290
Enter the expenses in day 21: 300
Enter the expenses in day 22: 310
Enter the expenses in day 23: 280
Enter the expenses in day 24: 295
Enter the expenses in day 25: 315
Enter the expenses in day 26: 305
Enter the expenses in day 27: 290
Enter the expenses in day 28: 320
Enter the expenses in day 29: 300
Enter the expenses in day 30: 310
Total Monthly Expense: ₹8975
'''

# Problem 29: Flight Luggage
# Definition
# A for loop with an if statement can count values based on a
# condition.
# Task
# Read the luggage weight of 20 passengers. Count how many
# passengers have luggage weighing more than 15 kg.
# Example Input
# 12
# 18
# 20
# 15
# 17
# 14
# 22
# 19
# 13
# 16
# 24
# 10
# 21
# 18
# 15
# 23
# 11
# 17
# 20
# 14
# Example Output
# Passengers With Luggage Above 15 kg: 12

count = 0
for passengers in range(1,21):
    luggage = int(input(f"Enter the weight of the passenger {passengers} luggage: "))
    if luggage>15:
        count+=1
print(f'Passengers With Luggage Above 15 kg: {count}')

'''
Output:
Enter the weight of the passenger 1 luggage: 12
Enter the weight of the passenger 2 luggage: 18
Enter the weight of the passenger 3 luggage: 20
Enter the weight of the passenger 4 luggage: 15
Enter the weight of the passenger 5 luggage: 17
Enter the weight of the passenger 6 luggage: 14
Enter the weight of the passenger 7 luggage: 22
Enter the weight of the passenger 8 luggage: 19
Enter the weight of the passenger 9 luggage: 13
Enter the weight of the passenger 10 luggage: 16
Enter the weight of the passenger 11 luggage: 24
Enter the weight of the passenger 12 luggage: 10
Enter the weight of the passenger 13 luggage: 21
Enter the weight of the passenger 14 luggage: 18
Enter the weight of the passenger 15 luggage: 15
Enter the weight of the passenger 16 luggage: 23
Enter the weight of the passenger 17 luggage: 11
Enter the weight of the passenger 18 luggage: 17
Enter the weight of the passenger 19 luggage: 20
Enter the weight of the passenger 20 luggage: 14
Passengers With Luggage Above 15 kg: 12
'''

# Problem 30: Store Inventory
# Definition
# A for loop and an if statement can count products based on
# stock availability.
# Task
# Read the stock quantity of 25 products. Count how many
# products have stock less than 10 units.
# Example Input
# 12
# 8
# 15
# 6
# 20
# 9
# 18
# 7
# 25
# 5
# 14
# 11
# 3
# 16
# 8
# 19
# 6
# 13
# 10
# 4
# 17
# 9
# 21
# 2
# 12
# Example Output
# Products With Stock Less Than 10 Units: 11

count = 0
for prod in range(1,26):
    stock = int(input(f"Enter the stock of products {prod}:"))
    if stock < 10:
        count+=1
print(f'Products With Stock Less Than 10 Units: {count}')

'''
Output:
Enter the stock of products 1:12
Enter the stock of products 2:8
Enter the stock of products 3:15
Enter the stock of products 4:6
Enter the stock of products 5:20
Enter the stock of products 6:9
Enter the stock of products 7:18
Enter the stock of products 8:7
Enter the stock of products 9:25
Enter the stock of products 10:5
Enter the stock of products 11:14
Enter the stock of products 12:11
Enter the stock of products 13:3
Enter the stock of products 14:16
Enter the stock of products 15:8
Enter the stock of products 16:19
Enter the stock of products 17:6
Enter the stock of products 18:13
Enter the stock of products 19:10
Enter the stock of products 20:4
Enter the stock of products 21:17
Enter the stock of products 22:9
Enter the stock of products 23:21
Enter the stock of products 24:2
Enter the stock of products 25:12
Products With Stock Less Than 10 Units: 11
'''

