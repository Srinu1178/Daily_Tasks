# 30 problems on while loop
# 1. Daily Water Intake
# Task: Read the amount of water (in liters) consumed each day for
# 7 days using a while loop. Find the total water consumed.
days = 7
i = 1
total = 0
while i<=days:
    water = int(input(f"Enter how much water (liters) consumed in day {i}:"))
    total+=water
    i+=1
print(f'The water was consumed in {days} days: {total}')

'''
Output:
Enter how much water (liters) consumed in day 1:3
Enter how much water (liters) consumed in day 2:2
Enter how much water (liters) consumed in day 3:1
Enter how much water (liters) consumed in day 4:4
Enter how much water (liters) consumed in day 5:2
Enter how much water (liters) consumed in day 6:3
Enter how much water (liters) consumed in day 7:1
The water was consumed in 7 days: 16
'''


# 2. Grocery Shopping
# Task: Read the prices of 10 grocery items using a while loop. Find
# the total bill amount.
items = 10
i = 1
bill = 0
while i<=items:
    price = int(input(f"Enter the price of item {i}: "))
    bill+=price
    i+=1
print(f'Total bill of {items} items is : {bill}')

'''
Output:
Enter the price of item 1: 180
Enter the price of item 2: 1200
Enter the price of item 3: 80
Enter the price of item 4: 180
Enter the price of item 5: 200
Enter the price of item 6: 220
Enter the price of item 7: 100
Enter the price of item 8: 300
Enter the price of item 9: 150
Enter the price of item 10: 40
Total bill of 10 items is : 2650
'''

# 3. Classroom Attendance
# Task: Read the attendance (Present or Absent) of 20 students.
# Count how many students are present.

students = 20
i = 1
count = 0
while i<=students:
    attendence = input(f"Enter the attendence of student {i}(Present or Absent): ")
    if attendence=="Present" or attendence=="present":
        count+=1
    i+=1
print(f'The students are present {count} out of {students} students')

'''
Output:
Enter the attendence of student 1(Present or Absent): present
Enter the attendence of student 2(Present or Absent): absent
Enter the attendence of student 3(Present or Absent): present
Enter the attendence of student 4(Present or Absent): present
Enter the attendence of student 5(Present or Absent): present
Enter the attendence of student 6(Present or Absent): absent
Enter the attendence of student 7(Present or Absent): absent
Enter the attendence of student 8(Present or Absent): present
Enter the attendence of student 9(Present or Absent): absent
Enter the attendence of student 10(Present or Absent): present
Enter the attendence of student 11(Present or Absent): present
Enter the attendence of student 12(Present or Absent): absent
Enter the attendence of student 13(Present or Absent): present
Enter the attendence of student 14(Present or Absent): present
Enter the attendence of student 15(Present or Absent): absent
Enter the attendence of student 16(Present or Absent): present
Enter the attendence of student 17(Present or Absent): absent
Enter the attendence of student 18(Present or Absent): present
Enter the attendence of student 19(Present or Absent): present
Enter the attendence of student 20(Present or Absent): present
The students are present 13 out of 20 students
'''

# 4. Cricket Tournament
# Task: Read the runs scored in 10 matches. Find the total runs
# scored.

matches = 10
i = 1
score = 0
while i<=matches:
    runs = int(input(f"Enter the runs in match {i}: "))
    score += runs
    i+=1
print(f'The total runs in {matches} matches: {score}')

'''
Output:
Enter the runs in match 1: 50
Enter the runs in match 2: 100
Enter the runs in match 3: 150
Enter the runs in match 4: 70
Enter the runs in match 5: 80
Enter the runs in match 6: 200
Enter the runs in match 7: 160
Enter the runs in match 8: 170
Enter the runs in match 9: 120
Enter the runs in match 10: 112
The total runs in 10 matches: 1212
'''


# 5. Fuel Station
# Task: Read the liters of fuel filled by 15 customers. Find the total
# liters sold.

customers = 15
i = 1
liters = 0
while i<=15:
    fuel = int(input(f"Enter the liters of fuel for customer {i}:"))
    liters += fuel
    i+=1
print(f'The total {liters} liters sold')

'''
Output:
Enter the liters of fuel for customer 6:8
Enter the liters of fuel for customer 7:15
Enter the liters of fuel for customer 8:20
Enter the liters of fuel for customer 9:4
Enter the liters of fuel for customer 10:9
Enter the liters of fuel for customer 11:15
Enter the liters of fuel for customer 12:10
Enter the liters of fuel for customer 13:3
Enter the liters of fuel for customer 14:15
Enter the liters of fuel for customer 15:2
The total 122 liters sold
'''

# 6. Employee Salaries
# Task: Read the salaries of 12 employees. Find the highest salary.

employees = 12
i = 1
highest = 0
while i<=employees:
    salary = int(input(f'Enter the salary of employee {i}: '))
    if salary>highest:
        highest = salary
    i+=1
print(f'The highest salary among the {employees} employees is : {highest}')

'''
Output:
Enter the salary of employee 1: 12000
Enter the salary of employee 2: 20000
Enter the salary of employee 3: 25000
Enter the salary of employee 4: 35000
Enter the salary of employee 5: 60000
Enter the salary of employee 6: 70000
Enter the salary of employee 7: 45000
Enter the salary of employee 8: 19000
Enter the salary of employee 9: 20000
Enter the salary of employee 10: 180000
Enter the salary of employee 11: 100000
Enter the salary of employee 12: 200000
The highest salary among the 20 employees is : 200000
'''

# 7. Bike Mileage
# Task: Read the mileage of 10 bikes. Find the average mileage.

bikes = 10
i = 1
total = 0
count = 0
while i<=bikes:
    mileage = int(input(f"Enter the mileage of bike {i}: "))
    total += mileage
    count+=1
    i+=1
avg = total/count
print(f'The average mileage of {bikes} bikes is: {avg:.2f} km/l')

'''
Output:
Enter the mileage of bike 1: 50
Enter the mileage of bike 2: 30
Enter the mileage of bike 3: 60
Enter the mileage of bike 4: 80
Enter the mileage of bike 5: 15
Enter the mileage of bike 6: 25
Enter the mileage of bike 7: 60
Enter the mileage of bike 8: 55
Enter the mileage of bike 9: 50
Enter the mileage of bike 10: 20
The average mileage of 10 bikes is: 44.50 km/l
'''


# 8. Mobile Recharge
# Task: Read the recharge amounts of 15 customers. Count how
# many customers recharged more than ₹500.

customers = 15
count = 0
i = 1
while i<=customers:
    recharge = int(input(f"Enter the recharge amount of customer {i}: "))
    if recharge > 500:
        count+=1
    i+=1
print(f'Customers above \u20B9500 recharge are {count} customers')

'''
Output:
Enter the recharge amount of customer 1: 299
Enter the recharge amount of customer 2: 399
Enter the recharge amount of customer 3: 550
Enter the recharge amount of customer 4: 599
Enter the recharge amount of customer 5: 899
Enter the recharge amount of customer 6: 750
Enter the recharge amount of customer 7: 2999
Enter the recharge amount of customer 8: 3999
Enter the recharge amount of customer 9: 350
Enter the recharge amount of customer 10: 666
Enter the recharge amount of customer 11: 799
Enter the recharge amount of customer 12: 899
Enter the recharge amount of customer 13: 1555
Enter the recharge amount of customer 14: 2999
Enter the recharge amount of customer 15: 769
Customers above ₹500 recharge are 12 customers
'''


# 9. Electricity Usage
# Task: Read electricity units used by 20 houses. Find the total
# units consumed.

houses = 20
i = 1
total = 0
while i<=houses:
    units = int(input(f"Enter the units consumed for house {i}: "))
    total += units
    i+=1
print(f'The total units consumed by {houses} houses is {total}')

'''
Output:
Enter the units consumed for house 1: 220
Enter the units consumed for house 2: 100 
Enter the units consumed for house 3: 150
Enter the units consumed for house 4: 120 
Enter the units consumed for house 5: 200
Enter the units consumed for house 6: 116
Enter the units consumed for house 7: 150
Enter the units consumed for house 8: 160
Enter the units consumed for house 9: 170
Enter the units consumed for house 10: 180 
Enter the units consumed for house 11: 175
Enter the units consumed for house 12: 143
Enter the units consumed for house 13: 149
Enter the units consumed for house 14: 150
Enter the units consumed for house 15: 160
Enter the units consumed for house 16: 155
Enter the units consumed for house 17: 165
Enter the units consumed for house 18: 170
Enter the units consumed for house 19: 180
Enter the units consumed for house 20: 190
The total units consumed by 20 houses is 3203
'''


# 10. Exam Results
# Task: Read the marks of 30 students. Count how many students
# passed (marks ≥ 35).

students = 30
i = 1
passed = 0
while i<=students:
    marks = int(input(f"Enter the marks of student {i}:"))
    if marks>=35:
        passed+=1
    i+=1
print(f'The students are passed {passed} out of {students} students')

'''
Output:
Enter the marks of student 1:40
Enter the marks of student 2:30
Enter the marks of student 3:25
Enter the marks of student 4:60
Enter the marks of student 5:70
Enter the marks of student 6:80
Enter the marks of student 7:66
Enter the marks of student 8:44
Enter the marks of student 9:35
Enter the marks of student 10:37
Enter the marks of student 11:89
Enter the marks of student 12:67
Enter the marks of student 13:77
Enter the marks of student 14:14
Enter the marks of student 15:67
Enter the marks of student 16:88
Enter the marks of student 17:44
Enter the marks of student 18:35
Enter the marks of student 19:56
Enter the marks of student 20:78
Enter the marks of student 21:34
Enter the marks of student 22:56
Enter the marks of student 23:78
Enter the marks of student 24:90
Enter the marks of student 25:53
Enter the marks of student 26:23
Enter the marks of student 27:40
Enter the marks of student 28:37
Enter the marks of student 29:66
Enter the marks of student 30:78
The students are passed 25 out of 30 students
'''


# 11. Hospital Patients
# Task: Read the ages of 20 patients. Count how many patients are
# senior citizens (age ≥ 60).
patients = 20
count = 0
i = 1
while i<=patients:
    age = int(input(f"Enter the age of patient {i}: "))
    if age>=60:
        count+=1
    i+=1
print(f'The senior patients are {count} out of {patients} patients')

'''
Output:
Enter the age of patient 1: 40
Enter the age of patient 2: 60
Enter the age of patient 3: 45
Enter the age of patient 4: 55
Enter the age of patient 5: 65
Enter the age of patient 6: 70
Enter the age of patient 7: 75
Enter the age of patient 8: 76
Enter the age of patient 9: 21
Enter the age of patient 10: 25
Enter the age of patient 11: 40
Enter the age of patient 12: 65
Enter the age of patient 13: 40
Enter the age of patient 14: 55
Enter the age of patient 15: 78
Enter the age of patient 16: 53
Enter the age of patient 17: 33
Enter the age of patient 18: 40
Enter the age of patient 19: 50  
Enter the age of patient 20: 70
The senior patients are 8 out of 20 patients
'''


# 12. Bus Passengers
# Task: Read the number of passengers entering the bus at 8
# stops. Find the total passengers.

stops = 8
i = 1
total = 0
while i <= stops:
    passengers = int(input(f"Enter the no of passengers bus at {i} stop: "))
    total+=passengers
    i+=1
print(f'The total no of passengers in {stops} stops are {total}')

'''
Output:
Enter the no of passengers bus at 1 stop: 10
Enter the no of passengers bus at 2 stop: 8
Enter the no of passengers bus at 3 stop: 5
Enter the no of passengers bus at 4 stop: 15
Enter the no of passengers bus at 5 stop: 7
Enter the no of passengers bus at 6 stop: 4
Enter the no of passengers bus at 7 stop: 3
Enter the no of passengers bus at 8 stop: 2
The total no of passengers in 8 stops are 54
'''


# 13. Cinema Tickets
# Task: Read the ticket prices of 25 customers. Find the total ticket
# collection.

customers = 25
i = 1
total = 0
while i<=customers:
    price = int(input(f"Enter the ticket price of customer {i}: "))
    total += price
    i+=1
print(f'The total ticket collection from {customers} customers is \u20b9{total}')

'''
Output:
Enter the ticket price of customer 1: 70
Enter the ticket price of customer 2: 150
Enter the ticket price of customer 3: 250
Enter the ticket price of customer 4: 70
Enter the ticket price of customer 5: 120
Enter the ticket price of customer 6: 250
Enter the ticket price of customer 7: 250
Enter the ticket price of customer 8: 150
Enter the ticket price of customer 9: 120
Enter the ticket price of customer 10: 70
Enter the ticket price of customer 11: 120
Enter the ticket price of customer 12: 150
Enter the ticket price of customer 13: 250
Enter the ticket price of customer 14: 120
Enter the ticket price of customer 15: 150
Enter the ticket price of customer 16: 120
Enter the ticket price of customer 17: 250
Enter the ticket price of customer 18: 250
Enter the ticket price of customer 19: 120
Enter the ticket price of customer 20: 70
Enter the ticket price of customer 21: 120
Enter the ticket price of customer 22: 70
Enter the ticket price of customer 23: 250
Enter the ticket price of customer 24: 250
Enter the ticket price of customer 25: 150
The total ticket collection from 25 customers is ₹3940
'''

# 14. Warehouse Boxes
# Task: Read the weight of 20 boxes. Find the heaviest box.

boxes = 20
i = 1
heavy = 0
box = 0
while i<=boxes:
    weight = int(input(f"Enter the weight of box {i} in kgs: "))
    if weight>heavy:
        heavy = weight
        box = i
    i+=1
print(f'The heavist box is {box} and the weight is {heavy} kgs')

'''
Output:
Enter the weight of box 1 in kgs: 25
Enter the weight of box 2 in kgs: 50
Enter the weight of box 3 in kgs: 40
Enter the weight of box 4 in kgs: 70
Enter the weight of box 5 in kgs: 100
Enter the weight of box 6 in kgs: 78
Enter the weight of box 7 in kgs: 90
Enter the weight of box 8 in kgs: 20
Enter the weight of box 9 in kgs: 36
Enter the weight of box 10 in kgs: 14
Enter the weight of box 11 in kgs: 60
Enter the weight of box 12 in kgs: 80
Enter the weight of box 13 in kgs: 90
Enter the weight of box 14 in kgs: 20
Enter the weight of box 15 in kgs: 35
Enter the weight of box 16 in kgs: 48
Enter the weight of box 17 in kgs: 18
Enter the weight of box 18 in kgs: 78
Enter the weight of box 19 in kgs: 66
Enter the weight of box 20 in kgs: 55
The heavist box is 5 and the weight is 100 kgs
'''


# 15. Phone Battery
# Task: Read the battery percentage of 15 phones. Count how
# many phones have battery below 20%.

phones = 15
i = 1
count = 0
while i<=phones:
    percentage = int(input(f'Enter the percentage of battery in phone {i}: '))
    if percentage<20:
        count+=1
    i+=1
print(f'Below 20% battery mobiles are {count} out of {phones} phones')

'''
Output
Enter the percentage of battery in phone 1: 20
Enter the percentage of battery in phone 2: 9
Enter the percentage of battery in phone 3: 10
Enter the percentage of battery in phone 4: 50
Enter the percentage of battery in phone 5: 60
Enter the percentage of battery in phone 6: 70
Enter the percentage of battery in phone 7: 10
Enter the percentage of battery in phone 8: 15
Enter the percentage of battery in phone 9: 19
Enter the percentage of battery in phone 10: 20
Enter the percentage of battery in phone 11: 18
Enter the percentage of battery in phone 12: 15
Enter the percentage of battery in phone 13: 18
Enter the percentage of battery in phone 14: 19
Enter the percentage of battery in phone 15: 25
Below 20% battery mobiles are 9 out of 15 phones
'''

# 16. Monthly Expenses
# Task: Read daily expenses for 30 days. Find the total monthly
# expense.

days = 30
i = 1
total = 0
while i<=days:
    expense = int(input(f"Enter the expense of day {i}: "))
    total += expense
    i+=1
print(f'The total expenses for {days} days is \u20B9{total}')

'''
Output:
Enter the expense of day 1: 250
Enter the expense of day 2: 100
Enter the expense of day 3: 500
Enter the expense of day 4: 600
Enter the expense of day 5: 800
Enter the expense of day 6: 70
Enter the expense of day 7: 900
Enter the expense of day 8: 1000
Enter the expense of day 9: 500
Enter the expense of day 10: 200
Enter the expense of day 11: 400
Enter the expense of day 12: 600 
Enter the expense of day 13: 400
Enter the expense of day 14: 600
Enter the expense of day 15: 100
Enter the expense of day 16: 300
Enter the expense of day 17: 180
Enter the expense of day 18: 220
Enter the expense of day 19: 170 
Enter the expense of day 20: 280
Enter the expense of day 21: 300
Enter the expense of day 22: 160
Enter the expense of day 23: 180
Enter the expense of day 24: 560
Enter the expense of day 25: 120
Enter the expense of day 26: 200
Enter the expense of day 27: 500
Enter the expense of day 28: 800
Enter the expense of day 29: 900
Enter the expense of day 30: 200
The total expenses for 30 days is ₹12090
'''

# 17. Hotel Room Rent
# Task: Read the room rent of 12 bookings. Find the highest room
# rent.

bookings = 12
i = 1
highest = 0
while i <= bookings:
    rent = int(input(f"Enter the room rent of booking {i}: "))
    if rent>highest:
        highest = rent
    i+=1

print(f'The highest room rent among the {bookings} bookings is \u20B9{highest}')

'''
Output:
Enter the room rent of booking 1: 700
Enter the room rent of booking 2: 900
Enter the room rent of booking 3: 1200
Enter the room rent of booking 4: 1000
Enter the room rent of booking 5: 500
Enter the room rent of booking 6: 1500
Enter the room rent of booking 7: 2500
Enter the room rent of booking 8: 3000
Enter the room rent of booking 9: 3500
Enter the room rent of booking 10: 1200
Enter the room rent of booking 11: 1000
Enter the room rent of booking 12: 1600
The highest room rent among the 12 bookings is ₹3500
'''

# 18. ATM Withdrawals
# Task: Read the withdrawal amounts of 15 customers. Count how
# many customers withdraw more than ₹10000.

customers = 15
i = 1
count = 1
while i<=customers:
    amount = int(input(f'Enter the withdrawl amount of customer {i}: '))
    if amount > 10000:
        count+=1
    i+=1
print(f'Above \u20B910000 withdraw amount customers {count} out of {customers}')

'''
Output:
Enter the withdrawl amount of customer 1: 3000 
Enter the withdrawl amount of customer 2: 10000
Enter the withdrawl amount of customer 3: 20000
Enter the withdrawl amount of customer 4: 15000
Enter the withdrawl amount of customer 5: 25000
Enter the withdrawl amount of customer 6: 10000
Enter the withdrawl amount of customer 7: 60000
Enter the withdrawl amount of customer 8: 6000
Enter the withdrawl amount of customer 9: 50000
Enter the withdrawl amount of customer 10: 18000
Enter the withdrawl amount of customer 11: 19000
Enter the withdrawl amount of customer 12: 22000
Enter the withdrawl amount of customer 13: 15000
Enter the withdrawl amount of customer 14: 12000
Enter the withdrawl amount of customer 15: 1000
Above ₹10000 withdraw amount customers 11 out of 15
'''

# 19. Product Ratings
# Task: Read the ratings (1–5) of 20 products. Count how many
# products received a rating of 5.

products = 20
i = 1
count = 0
while i<=products:
    rating = int(input(f"Enter the rating of product {i}: "))
    if rating == 5:
        count+=1
    i+=1
print(f'The products of rating 5 are {count} out of {products}' )

'''
Output:
Enter the rating of product 1: 5
Enter the rating of product 2: 4
Enter the rating of product 3: 3
Enter the rating of product 4: 2
Enter the rating of product 5: 5
Enter the rating of product 6: 4
Enter the rating of product 7: 5
Enter the rating of product 8: 5
Enter the rating of product 9: 5
Enter the rating of product 10: 2
Enter the rating of product 11: 4
Enter the rating of product 12: 5
Enter the rating of product 13: 5
Enter the rating of product 14: 4
Enter the rating of product 15: 2
Enter the rating of product 16: 3
Enter the rating of product 17: 5
Enter the rating of product 18: 2
Enter the rating of product 19: 4
Enter the rating of product 20: 5
The products of rating 5 are 9 out of 20
'''

# 20. Internet Data Usage
# Task: Read daily internet usage (GB) for 30 days. Find the total
# data used.

days = 30
i = 1
total = 0
while i<=days:
    data = float(input(f'Enter the data used for day {i} in GB: '))
    total += data
    i+=1
print(f"The data is used for {days} days is: {total:.2f}")

'''
Output:
Enter the data used for day 1 in GB: 3
Enter the data used for day 2 in GB: 1.5
Enter the data used for day 3 in GB: 2
Enter the data used for day 4 in GB: 2.5
Enter the data used for day 5 in GB: 2
Enter the data used for day 6 in GB: 1.5
Enter the data used for day 7 in GB: 1.2
Enter the data used for day 8 in GB: 1
Enter the data used for day 9 in GB: 1.8
Enter the data used for day 10 in GB: 2.3
Enter the data used for day 11 in GB: 3
Enter the data used for day 12 in GB: 3.2
Enter the data used for day 13 in GB: 2.1
Enter the data used for day 14 in GB: 1
Enter the data used for day 15 in GB: 1.5
Enter the data used for day 16 in GB: 2.5
Enter the data used for day 17 in GB: 1.2
Enter the data used for day 18 in GB: 1.5
Enter the data used for day 19 in GB: 1 
Enter the data used for day 20 in GB: 3 
Enter the data used for day 21 in GB: 1
Enter the data used for day 22 in GB: 2
Enter the data used for day 23 in GB: 1.2
Enter the data used for day 24 in GB: 2.6
Enter the data used for day 25 in GB: 2.3
Enter the data used for day 26 in GB: 1.4
Enter the data used for day 27 in GB: 1.2
Enter the data used for day 28 in GB: 1.2
Enter the data used for day 29 in GB: 1.3
Enter the data used for day 30 in GB: 1.8
The data is used for 30 days is: 54.80
'''

# 21. Flight Luggage
# Task: Read the luggage weight of 20 passengers. Count how
# many passengers have luggage above 15 kg.

passengers = 20
i = 1
count = 0
while i<=passengers:
    weight = int(input(f"Enter the luggage weight of passenger {i}: "))
    if weight>15:
        count+=1
    i+=1
print(f'The no of passengers luggage weight above 15 kg are {count} out of {passengers} passengers')

'''
Output:
Enter the luggage weight of passenger 1: 20
Enter the luggage weight of passenger 2: 10
Enter the luggage weight of passenger 3: 50
Enter the luggage weight of passenger 4: 20
Enter the luggage weight of passenger 5: 8
Enter the luggage weight of passenger 6: 9
Enter the luggage weight of passenger 7: 5
Enter the luggage weight of passenger 8: 10
Enter the luggage weight of passenger 9: 17
Enter the luggage weight of passenger 10: 20
Enter the luggage weight of passenger 11: 21
Enter the luggage weight of passenger 12: 22
Enter the luggage weight of passenger 13: 19
Enter the luggage weight of passenger 14: 20
Enter the luggage weight of passenger 15: 15
Enter the luggage weight of passenger 16: 20
Enter the luggage weight of passenger 17: 18
Enter the luggage weight of passenger 18: 29
Enter the luggage weight of passenger 19: 30
Enter the luggage weight of passenger 20: 15
The no of passengers luggage weight above 15 kg are 13 out of 20 passengers
'''

# 22. Water Bottles
# Task: Read the capacity of 15 water bottles. Find the smallest
# bottle capacity.

bottles = 15
smallest = float("inf")
i = 1
while i<=15:
    capacity = int(input(f"Enter the capacity of bottle(in ml) {i}: "))
    if capacity<smallest:
        smallest=capacity
    i+=1
print(f'The smallest capacity of bottle is: {smallest} ml')

'''
Output:
Enter the capacity of bottle(in ml) 1: 200
Enter the capacity of bottle(in ml) 2: 250
Enter the capacity of bottle(in ml) 3: 350
Enter the capacity of bottle(in ml) 4: 750
Enter the capacity of bottle(in ml) 5: 500
Enter the capacity of bottle(in ml) 6: 1000
Enter the capacity of bottle(in ml) 7: 800
Enter the capacity of bottle(in ml) 8: 900
Enter the capacity of bottle(in ml) 9: 400 
Enter the capacity of bottle(in ml) 10: 750
Enter the capacity of bottle(in ml) 11: 200
Enter the capacity of bottle(in ml) 12: 250
Enter the capacity of bottle(in ml) 13: 800
Enter the capacity of bottle(in ml) 14: 150
Enter the capacity of bottle(in ml) 15: 200
The smallest capacity of bottle is: 150 ml
'''

# 23. Online Orders
# Task: Read the values of 20 online orders. Count how many
# orders are above ₹1000.

orders = 20
i = 1
count = 0
while i<=orders:
    price = int(input(f"Enter the price of order {i}: "))
    if price>1000:
        count+=1
    i+=1
print(f'The number of orders above \u20B91000 are {count} out of {orders}')

'''
Output:
Enter the price of order 1: 1200 
Enter the price of order 2: 500 
Enter the price of order 3: 1300 
Enter the price of order 4: 1500 
Enter the price of order 5: 1400 
Enter the price of order 6: 800
Enter the price of order 7: 1000
Enter the price of order 8: 1100
Enter the price of order 9: 900
Enter the price of order 10: 1500
Enter the price of order 11: 2000
Enter the price of order 12: 1800
Enter the price of order 13: 2000
Enter the price of order 14: 600 
Enter the price of order 15: 700
Enter the price of order 16: 500
Enter the price of order 17: 890
Enter the price of order 18: 1540
Enter the price of order 19: 2345
Enter the price of order 20: 3000
The number of orders above ₹1000 are 12 out of 20
'''


# 24. Rainfall Record
# Task: Read rainfall (mm) for 12 months. Find the highest rainfall.

months = 12
i = 1
highest = 0
while i<=months:
    rain = float(input(f'Enter the rainfall(mm) in month {i}: '))
    if rain>highest:
        highest = rain
    i+=1
print(f'The highest rainfall is {highest} mm')

'''
Output
Enter the rainfall(mm) in month 1: 70
Enter the rainfall(mm) in month 2: 100
Enter the rainfall(mm) in month 3: 56.8
Enter the rainfall(mm) in month 4: 77.7
Enter the rainfall(mm) in month 5: 80.8
Enter the rainfall(mm) in month 6: 78 
Enter the rainfall(mm) in month 7: 50
Enter the rainfall(mm) in month 8: 44.44
Enter the rainfall(mm) in month 9: 55
Enter the rainfall(mm) in month 10: 77.9
Enter the rainfall(mm) in month 11: 45.5
Enter the rainfall(mm) in month 12: 60.7
The highest rainfall is 100.0 mm
'''

# 25. School Fees
# Task: Read the fees paid by 15 students. Find the total amount
# collected.

students = 15
i = 1
total = 0
while i<=students:
    amount = int(input(f'Enter the fee amount of student {i}: '))
    total+=amount
    i+=1

print(f'The total amount of {students} students is: \u20B9{total}')

'''
Output:
Enter the fee amount of student 1: 30000
Enter the fee amount of student 2: 20000
Enter the fee amount of student 3: 50000
Enter the fee amount of student 4: 10000
Enter the fee amount of student 5: 300000
Enter the fee amount of student 6: 400000
Enter the fee amount of student 7: 500000
Enter the fee amount of student 8: 78000
Enter the fee amount of student 9: 89000
Enter the fee amount of student 10: 90000
Enter the fee amount of student 11: 200000
Enter the fee amount of student 12: 250000
Enter the fee amount of student 13: 300000
Enter the fee amount of student 14: 400000
Enter the fee amount of student 15: 500000
The total amount of 15 students is: ₹3217000
'''

# 26. Car Speeds
# Task: Read the speed of 20 cars. Count how many cars
# exceeded 80 km/h.

cars = 20
i = 1
count = 0
while i<=cars:
    speed = int(input(f'Enter the speed of car {i}: '))
    if speed>80:
        count+=1
    i+=1
print(f'The number of cars above 80 km/h are {count} out of {cars}')

'''
Output:
Enter the speed of car 1: 40
Enter the speed of car 2: 60
Enter the speed of car 3: 90
Enter the speed of car 4: 85
Enter the speed of car 5: 120
Enter the speed of car 6: 110
Enter the speed of car 7: 117
Enter the speed of car 8: 102
Enter the speed of car 9: 100
Enter the speed of car 10: 96
Enter the speed of car 11: 69
Enter the speed of car 12: 70
Enter the speed of car 13: 50
Enter the speed of car 14: 89
Enter the speed of car 15: 88
Enter the speed of car 16: 97
Enter the speed of car 17: 123
Enter the speed of car 18: 120
Enter the speed of car 19: 98
Enter the speed of car 20: 88
The number of cars above 80 km/h are 15 out of 20
'''

# 27. Library Books
# Task: Read the number of pages in 15 books. Find the book with
# the maximum pages.

books = 15
i = 1
book = 0
maximum = 0
while i<=books:
    pages = int(input(f"Enter the no of pages in book {i}: "))
    if pages>maximum:
        maximum = pages
        book = i
    i+=1
print(f'The maximum no of pages is {maximum} and the book is book {book}')

'''
Output:
Enter the no of pages in book 1: 100
Enter the no of pages in book 2: 250
Enter the no of pages in book 3: 400
Enter the no of pages in book 4: 550
Enter the no of pages in book 5: 600
Enter the no of pages in book 6: 150
Enter the no of pages in book 7: 250
Enter the no of pages in book 8: 450
Enter the no of pages in book 9: 150
Enter the no of pages in book 10: 100
Enter the no of pages in book 11: 170
Enter the no of pages in book 12: 190
Enter the no of pages in book 13: 289
Enter the no of pages in book 14: 299
Enter the no of pages in book 15: 270
The maximum no of pages is 600 and the book is book 5
'''

# 28. Store Inventory
# Task: Read the stock quantity of 25 products. Count how many
# products have stock less than 10 units.

products = 25
i = 1
count = 0
while i<=products:
    quantity = int(input(f"Enter the quantity of product {i}: "))
    if quantity<10:
        count+=1
    i+=1
print(f'The products are below 10 units are {count} out of {products} ')

'''
Output:
Enter the quantity of product 1: 6
Enter the quantity of product 2: 9
Enter the quantity of product 3: 8
Enter the quantity of product 4: 10
Enter the quantity of product 5: 20
Enter the quantity of product 6: 8
Enter the quantity of product 7: 10
Enter the quantity of product 8: 17
Enter the quantity of product 9: 20
Enter the quantity of product 10: 4
Enter the quantity of product 11: 8
Enter the quantity of product 12: 17
Enter the quantity of product 13: 28
Enter the quantity of product 14: 28
Enter the quantity of product 15: 29
Enter the quantity of product 16: 15
Enter the quantity of product 17: 24
Enter the quantity of product 18: 25
Enter the quantity of product 19: 27
Enter the quantity of product 20: 19
Enter the quantity of product 21: 20
Enter the quantity of product 22: 14
Enter the quantity of product 23: 16
Enter the quantity of product 24: 12
Enter the quantity of product 25: 10
The products are below 10 units are 6 out of 25 
'''
    

# 29. Courier Service
# Task: Read the parcel weight of 20 customers. Count how many
# parcels weigh more than 10 kg.

customers = 20
i = 1
count = 0
while i<=customers:
    weight = int(input(f'Enter the parcel weight of customer {i}: '))
    if weight>10:
        count+=1
    i+=1

print(f'The no of customers parcel weight above 10 kgs are {count} out of {customers}')


'''
Output:
Enter the parcel weight of customer 1: 40
Enter the parcel weight of customer 2: 12
Enter the parcel weight of customer 3: 6
Enter the parcel weight of customer 4: 8
Enter the parcel weight of customer 5: 9
Enter the parcel weight of customer 6: 10
Enter the parcel weight of customer 7: 50
Enter the parcel weight of customer 8: 20
Enter the parcel weight of customer 9: 16
Enter the parcel weight of customer 10: 8
Enter the parcel weight of customer 11: 10
Enter the parcel weight of customer 12: 19
Enter the parcel weight of customer 13: 25
Enter the parcel weight of customer 14: 70
Enter the parcel weight of customer 15: 100
Enter the parcel weight of customer 16: 50
Enter the parcel weight of customer 17: 25
Enter the parcel weight of customer 18: 67
Enter the parcel weight of customer 19: 45
Enter the parcel weight of customer 20: 25
The no of customers parcel weight above 10 kgs are 14 out of 20
'''


# 30. Employee Working Hours
# Task: Read the working hours of 30 employees. Count how many
# employees worked more than 8 hours.

employees = 30
i = 1
count = 0
while i<=employees:
    hours = int(input(f"Enter the working hours of customer {i}: "))
    if hours>8:
        count+=1
    i+=1
print(f"The number of employees working more than 8 hours are {count} out of {employees}")

'''
Output:
Enter the working hours of customer 1: 8
Enter the working hours of customer 2: 10
Enter the working hours of customer 3: 7
Enter the working hours of customer 4: 5
Enter the working hours of customer 5: 4
Enter the working hours of customer 6: 12
Enter the working hours of customer 7: 1
Enter the working hours of customer 8: 11
Enter the working hours of customer 9: 12
Enter the working hours of customer 10: 10
Enter the working hours of customer 11: 9
Enter the working hours of customer 12: 6
Enter the working hours of customer 13: 10
Enter the working hours of customer 14: 12
Enter the working hours of customer 15: 9
Enter the working hours of customer 16: 5
Enter the working hours of customer 17: 6
Enter the working hours of customer 18: 8
Enter the working hours of customer 19: 9
Enter the working hours of customer 20: 10
Enter the working hours of customer 21: 4
Enter the working hours of customer 22: 2
Enter the working hours of customer 23: 12
Enter the working hours of customer 24: 11
Enter the working hours of customer 25: 10
Enter the working hours of customer 26: 9
Enter the working hours of customer 27: 8
Enter the working hours of customer 28: 7
Enter the working hours of customer 29: 4
Enter the working hours of customer 30: 9
The number of employees working more than 8 hours are 16 out of 30
'''


