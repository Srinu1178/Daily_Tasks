# Problem 1: ATM Withdrawal Definition Nested if-else 
# statements are used when one condition needs 
# to be checked only after another condition is true. 
# Task Read the account balance and withdrawal amount.
# If the balance is sufficient: 
# If the withdrawal amount is a multiple of 100, alow the withdrawal. 
# Otherwise, print Enter amount in multiples of 100. Otherwise, 
# print Insufficient Balance. 
# Example Input Enter Account Balance: 25000 
# Enter Withdrawal Amount: 4500 
# Example Output Withdrawal Successful 

balance = int(input("Enter the balance: "))

if balance>0:
    withdrawl = int(input("Enter the withdrawl amount: "))
    if withdrawl%100==0 and balance>withdrawl:
        print("Withdrawl Sucessful")
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient Balance")

'''
Output:
Enter the balance: 1000
Enter the withdrawl amount: 500
Withdrawl Sucessful
'''

# Problem 2: Online Shopping Discount Definition 
# Use nested if-else statements to decide the discount based 
# on purchase amount and membership status. 
# Task Read the purchase amount and whether the customer is a premium member.
# If purchase amount is greater than ₹1000:
# If the customer is a premium member, 
# give a 20% discount. Otherwise, give a 10% discount. 
# Otherwise, no discount.
#  Example Input Purchase Amount: 3500 
# Premium Member: True 
# Example Output 20% Discount Applied

amount = int(input("Enter the amount: "))
if amount > 1000:
    is_premium = input("Are you premium member: yes or no: ")
    if is_premium=="yes":
        print("20% Discount Applied")
    else:
        print("10% Discount Applied")
else:
    print("No Discount")

'''
Output:
Enter the amount: 3500
Are you premium member: yes or no: yes
20% Discount Applied
'''

#  Problem 3: College Admission Definition Nested conditions 
# can check multiple eligibility requirements before making a decision. 
# Task Read marks and age. If marks are at least 60: 
# If age is at least 17, admission is approved. 
# Otherwise, print Age Not Eligible.
#  Otherwise, print Marks Not Eligible.
#  Example Input Marks: 72 
#  Age: 18 
# Example Output Admission Approved

marks = int(input("Enter the marks: "))
if marks>60:
    age = int(input("Enter the age: "))
    if age>17:
        print("Admission Approved")
    else:
        print("Age is Not Eligible")
else:
    print("Marks Not Eligible")

'''
Output:
Enter the marks: 72
Enter the age: 18
Admission Approved
'''


#  Problem 4: Login System Definition Nested if statements are commonly
#  used to verify login credentials step by step.
#  Task Read username and password. If the username is correct:
#  If the password is correct, login successful. 
#  Otherwise, print Incorrect Password. Otherwise, print Invalid Username.
#  Example Input Username: admin Password: admin123 
#  Example Output Login Successful

username = input("Enter the username: ")
if username == "admin":
    password = input("Enter the password: ")
    if password=="admin123":
        print("Login Sucessful")
    else:
        print("Incorrect Password")
else:
    print("Invalid Username")

'''
Output:
else_nested_else.py
Enter the username: admin
Enter the password: admin123
Login Sucessful
'''

#  Problem 5: Movie Booking Definition Nested conditions 
# help verify multiple requirements before confirming a booking. 
# Task Read age and seat availability. If age is 18 or above:
#  If seats are available, booking is successful. Otherwise, print House Full.
#  Otherwise, print Not Eligible. 
# Example Input Age: 25 Seats 
# Available: True 
# Example Output Booking Successful

age = int(input('Enter the age: '))
if age>=18:
    is_available = input("Is this seat available: yes or no: ")
    if is_available=="yes":
        print("Booking Successful")
    else:
        print("House Full")
else:
    print("Not Eligible")

'''
Output:
Enter the age: 25
Is this seat available: yes or no: yes
Booking Successful
'''


#  Problem 6: Library Membership Definition Nested conditions
#  can verify membership before checking borrowing eligibility. 
# Task Read membership status and number of overdue books. 
# If the user is a member: If overdue books are 0, alow borrowing.
#  Otherwise, print Pay Fine First. Otherwise, print Register First. 
# Example Input Member: True 
# Overdue Books: 0 
# Example Output Book Issued

is_member = input("Are you member: yes or no: ")
if is_member=='yes':
    overdue_books = int(input("Enter the overdue books: "))
    if overdue_books==0:
        print("Book Issued")
    else:
        print("Pay Fine First")
else:
    print("Register First")

'''
Output:
Are you member: yes or no: yes
Enter the overdue books: 0
Book Issued
'''

#  Problem 7: Hospital Appointment Definition Use nested conditions
#  to verify appointment details before alowing consultation.
#  Task Read appointment status and doctor availability. 
# If an appointment is booked: If the doctor is available, 
# consultation begins. Otherwise, print Please Wait. Otherwise, print 
# Book an Appointment First. 
# Example Input Appointment Booked: True 
# Doctor Available: True 
# Example Output Consultation Started 

is_book_appointment = input("Have you appointment: True Or False: ")
if is_book_appointment.lower()=='true':
    is_doctor_available = input("Is doctor available: True or False: ")
    if is_doctor_available.lower()=='true':
        print("Consultation Started")
    else:
        print("Please Wait")
else:
    print("Book an Appointment First")

'''
Output:
Have you appointment: True Or False: True
Is doctor available: True or False: True
Consultation Started
'''


# Problem 8: Flight Boarding Definition Nested conditions ensure all 
# required documents are verified before boarding.
#  Task Read passport availability and ticket confirmation.
#  If passport is available: If the ticket is confirmed, a low boarding. 
# Otherwise, print Ticket Not Confirmed. Otherwise, print Passport Required. 
# Example Input Passport Available: True 
# Ticket Confirmed: True Example 
# Output Boarding Alowed

is_passport_available = input("Have you passport True or False:")
if is_passport_available.lower()=='true':
    is_ticket_confirmed = input("Is ticket confirmed True or False: ")
    if is_ticket_confirmed.lower()=='true':
        print("Boarding allowed")
    else:
        print("Ticket Not Confirmed")
else:
    print("Passport is required")

'''
Output:
Have you passport True or False:True
Is ticket confirmed True or False: True
Boarding allowed
'''

# Problem 9: Driving License Definition Nested conditions help verify age
#  before checking test qualification. Task Read age and learner's test result. 
# If age is at least 18: If the learner's test is passed, issue the license. 
# Otherwise, print Retake Learner's Test. Otherwise, print Underage. 
# Example Input Age: 20 
# Learner Test Passed: True 
# Example Output License Issued 

age = int(input("Enter the age: "))
if age>=18:
    is_test_passed = input("are you passed test : True or False: ")
    if is_test_passed.lower()=='true':
        print("Licensed Issued")
    else:
        print("Retake Learners Test")
else:
    print("The person is underage")

'''
Output:
Enter the age: 20
are you passed test : True or False: True
Licensed Issued
'''

# Problem 10: Hotel Check-in Definition 
# Nested if-else statements are used to verify booking and identity 
# before check-in. Task Read booking status and ID proof availability. 
# If booking exists: If ID proof is available, a low check-in. Otherwise,
# print ID Proof Required. Otherwise, print Booking Not Found. 
# Example Input Booking Available: True ID Proof Available: True 
# Example Output Check-in Successful 

is_booking_available = input("Are you booking True or False: ")

if is_booking_available.lower()=='true':
    is_id_available = input("Have you Id proof: True or False: ")
    if is_id_available.lower()=='true':
        print('Check in successful')
    else:
        print("Id proof is required")
else:
    print("Booking Not Found")

'''
Output:
Are you booking True or False: True
Have you Id proof: True or False: True
Check in successful
'''

# Problem 11: Cricket Team Selection Definition Nested if-else statements are used 
# to check multiple conditions before selecting a player. 
# Task Read the runs scored and fitness test result. 
# If runs scored are at least 50: If the fitness test is passed, 
# select the player. Otherwise, print Fitness Test Failed. 
# Otherwise, print Not Selected.
# Example Input Runs Scored: 68 Fitness 
# Test Passed: True 
# Example Output Player Selected 

runs = int(input("Runs Scored: "))
if runs>=50:
    is_test_passed = input("Fitness Test Passed: ")
    if is_test_passed.lower()=='true':
        print("Player Selected")
    else:
        print("Fitness Test Failed")
else:
    print("Not Selected")

'''
Output:
Runs Scored: 65
Fitness Test Passed: True
Player Selected
'''

# Problem 12: Employee Promotion Definition Use nested conditions
#  to verify both work experience and performance before promoting an employee. 
# Task Read years of experience and performance rating.
#  If experience is at least 5 years: If performance rating is 8 or above, 
# promote the employee. Otherwise, print Promotion Delayed. Otherwise,
#  print Insufficient Experience. Example Input Years of Experience: 7 
# Performance Rating: 9
#  Example Output Promotion Approved 

exp = int(input("Years of Experience: "))
if exp>=5:
    rating = int(input("Performance Rating: "))
    if rating >=8:
        print("Promotion Approved")
    else:
        print("Promotion Delayed")
else:
    print("Insufficient Experience")

'''
Output:
Years of Experience: 7
Performance Rating: 9
Promotion Approved
'''

# Problem 13: Scholarship Eligibility Definition Nested conditions help 
# verify academic performance before checking financial eligibility. 
# Task Read percentage and annual family income. If percentage is at least 85: 
# If annual family income is less than ₹300000, approve the scholarship. 
# Otherwise, print Income Exceeds Limit. Otherwise, print Insufficient Marks. 
# Example Input Percentage: 91 
# Family Income: 250000
# Example Output Scholarship Approved 

percentage = int(input("Percentage: "))
if percentage>=81:
    annual_income = int(input("Income: "))
    if annual_income<300000:
        print("Scholorship Approved")
    else:
        print("Income Exceeds Limit")
else:
    print("Insufficient Marks")

'''
Output:
Percentage: 91
Income: 250000
Scholorship Approved
'''

# Problem 14: Mobile Recharge Definition Nested if-else statements 
# can be used to verify recharge amount and payment status. 
# Task Read recharge amount and payment status.
# If recharge amount is at least ₹199: If payment is successful, 
# complete the recharge. Otherwise, print Payment Failed.
#  Otherwise, print Minimum Recharge Required. 
# Example Input Recharge Amount: 299 
# Payment Successful: True 
# Example Output Recharge Successful 

amount = int(input("Recharge Amount: "))
if amount>199:
    is_payment_sucessful = input("Payment Successful: ")
    if is_payment_sucessful.lower()=='true':
        print("Recharge Successful")
    else:
        print("Payment Failed")
else:
    print("Minimum Recharge Required")

'''
Output:
Recharge Amount: 299
Payment Successful: True
Recharge Successful
'''

# Problem 15: Food Delivery Definition Nested conditions help determine
#  whether an order can be accepted. Task Read restaurant status and 
# delivery partner availability. If the restaurant is open:
#  If a delivery partner is available, accept the order. 
# Otherwise, print No Delivery Partner Available. Otherwise, 
# print Restaurant Closed. 
# Example Input Restaurant Open: True 
# Delivery Partner Available: True
#  Example Output Order Accepted 

rest_status = input("Restaurant Open: ")
if rest_status.lower()=='true':
    delivery_part_available = input("Delivery Partner Available: ")
    if delivery_part_available.lower()=='true':
        print("Order Accepted")
    else:
        print("No Delivery Partner Available")
else:
    print("Restaurant Closed")

'''
Output:
Restaurant Open: True
Delivery Partner Available: True
Order Accepted
'''


# Problem 16: Train Reservation Definition Nested conditions verify 
# seat availability before confirming payment. 
# Task Read seat availability and payment status. 
# If seats are available: If payment is completed, 
# confirm the ticket. Otherwise, print Complete Payment First. 
# Otherwise, print Waiting List. 
# Example Input Seats Available: True 
# Payment Completed: True 
# Example Output Ticket Confirmed 

is_seat = input("Seat Available: ")
if is_seat.lower()=="true":
    is_payement = input("Payment Completed: ")
    if is_payement.lower()=='true':
        print("Ticket Confirmed")
    else:
        print("Complete Payment First")
else:
    print("Waiting List")

'''
Output: 
Seat Available: True
Payment Completed: True
Ticket Confirmed
'''


# Problem 17: Online Exam Definition Nested if-else statements 
# ensure a l exam requirements are satisfied. 
# Task Read internet connection status and webcam status.
#  If the internet is available: If the webcam is enabled, 
# start the exam. Otherwise, print Enable Webcam. Otherwise,
#  print Connect to the Internet. 
# Example Input Internet Available: True 
# Webcam Enabled: True 
# Example Output Exam Started 

internet = input("Internet Available: ")
if internet.lower()=='true':
    webcam = input("Webcam Enabled: ")
    if webcam.lower()=='true':
        print('Exam Started')
    else:
        print("Enable Webcam")
else:
    print("Connect to the Internet")

'''
Output:
Internet Available: True
Webcam Enabled: True
Exam Started
'''


# Problem 18: Bike Rental Definition Nested conditions verify
# eligibility before renting a bike.
# Task Read driving license status and bike availability. 
# If the customer has a driving license: If a bike is available,
# approve the rental. Otherwise, print No Bikes Available.
# Otherwise, print Driving License Required. 
# Example Input Driving License: True 
# Bike Available: True 
# Example Output Bike Rental Approved

driving_license = input("Driving License: ")
if driving_license.lower()=='true':
    is_available = input("Bike Available: ")
    if is_available.lower()=='true':
        print("Rental Approved")
    else:
        print("No Bikes Available")
else:
    print("Driving License Required")

'''
Output:
Driving License: True
Bike Available: True
Rental Approved
'''


# Problem 19: Bank Loan Definition Nested conditions 
# verify salary before checking credit score.
#  Task Read monthly salary and credit score.
#  If monthly salary is at least ₹30000:
#  If credit score is at least 700, approve the loan. Otherwise,
# print Poor Credit Score. Otherwise, print Salary Too Low. 
# Example Input Monthly Salary: 45000 
# Credit Score: 760
#  Example Output Loan Approved 

salary = int(input("Monthly Salary: "))
if salary>=30000:
    credit_score=int(input("Credit Score: "))
    if credit_score>=700:
        print("Loan Approved")
    else:
        print("Poor Credit Score")
else:
    print("Salary Too Low")

'''
Output:
Monthly Salary: 45000
Credit Score: 760
Loan Approved
'''

# Problem 20: Cinema Entry Definition Nested if-else statements 
# verify ticket ownership before checking ticket validity.
# Task Read ticket availability and ticket validity. 
# If the customer has a ticket: If the ticket is valid, a low entry. 
# Otherwise, print Invalid Ticket. Otherwise, print Buy a Ticket First.
# Example Input Ticket Available: True 
# Ticket Valid: True 
# Example Output Entry Alowed 

ticket_available = input("Ticket Available: ")
if ticket_available.lower()=='true':
    is_valid = input("Ticket Valid: ")
    if is_valid.lower()=='true':
        print("Entry Allowed")
    else:
        print("Invalid Ticket")
else:
    print("Buy a Ticket First")

'''
Output:
Ticket Available: True
Ticket Valid: True
Entry Allowed
'''

# Problem 21: Gym Admission Definition Nested if-else statements
# help verify multiple eligibility conditions before granting admission. 
# Task Read the person's age and whether they have a medical fitness certificate. 
# If age is at least 18: If a medical fitness certificate is available, 
# approve the admission. Otherwise, print Medical Certificate Required. 
# Otherwise, print Not Eligible for Gym Admission.
# Example Input Age: 22 
# Medical Certificate: True 
# Example Output Gym Admission Approved 

age = int(input("Age: "))
if age>=18:
    medical_certificate = input("Medical Certificate: ")
    if medical_certificate.lower()=='true':
        print("Gym Admission Approved")
    else:
        print("Medical Certificate Required")
else:
    print("Not Eligible for GYM Admission")

'''
Output:
Age: 22
Medical Certificate: True
Gym Admission Approved
'''

# Problem 22: Company Interview Definition Nested conditions are used to check
# educational qualification before checking test results. 
# Task Read whether the candidate has completed a degree and whether
#  they passed the aptitude test. If the degree is completed:
#  If the aptitude test is passed, schedule the interview. Otherwise, 
# print Aptitude Test Failed. Otherwise, print Degree Required. 
# Example Input Degree Completed: True Aptitude Test Passed: True 
# Example Output Interview Scheduled 

has_degree = input("Degree Completed: ")
if has_degree.lower()=='true':
    is_passed = input("Aptitude Test Passed: ")
    if is_passed.lower()=='true':
        print("Interview Scheduled")
    else:
        print("Aptitude test failed")
else:
    print("Degree Required")

'''
Output:
Degree Completed: True
Aptitude Test Passed: True
Interview Scheduled
'''

# Problem 23: Courier Service Definition Nested if-else statements are useful
#  when one condition depends on another. 
# Task Read parcel weight and whether the delivery address is serviceable.
#  If parcel weight is 20 kg or less: If the address is serviceable, 
# accept the parcel. Otherwise, print Delivery Area Not Serviceable.
#  Otherwise, print Parcel Exceeds Weight Limit.
#  Example Input Parcel Weight: 12 
# Address Serviceable: True 
# Example Output Parcel Accepted 

weight = int(input("Parcel Weight: "))
if weight<=20:
    is_address_service = input("Address Serviceable: ")
    if is_address_service.lower()=='true':
        print("Parcel Accepted")
    else:
        print("Delivery area not serviceable")
else:
    print("Parcel Exceeds Weight Limit")

'''
Output:
Parcel Weight: 12
Address Serviceable: True
Parcel Accepted
'''

# Problem 24: Water Supply Definition Nested conditions help determine the correct
#  action based on water level and motor status. Task Read water tank level and motor
#  status. If the water level is below 20%: If the motor is working, fil the tank. 
# Otherwise, print Repair the Motor. Otherwise, print Water Level is Sufficient. 
# Example Input Water Level: 15 
# Motor Working: True 
# Example Output Fi ling Water Tank

water_tank_level = int(input("Water Level: "))
if water_tank_level<20:
    motor_status = input("Motor Working: ")
    if motor_status.lower()=='true':
        print("Filling Water Tank")
    else:
        print("Repair the motor")
else:
    print("Water Level is Sufficient")

'''
Output:
Water Level: 15
Motor Working: True
Filling Water Tank
'''

#  Problem 25: Smart Door Lock Definition Nested conditions can be used for multi-level
#  security verification. Task Read fingerprint match status and PIN verification status. 
# If the fingerprint matches: If the PIN is correct, unlock the door.
#  Otherwise, print Incorrect PIN. Otherwise, print Fingerprint Not Recognized.
#  Example Input Fingerprint Match: True 
# PIN Correct: True 
# Example Output Door Unlocked 

is_match = input("Fingerprint Match: ")
if is_match.lower()=="true":
    is_correct=input("PIN Correct: ")
    if is_correct.lower()=='true':
        print("Door Unlocked")
    else:
        print("Incorrect PIN")
else:
    print("Fingerprint Not Recognized")

'''
Output:
Fingerprint Match: True
PIN Correct: True
Door Unlocked
'''

# Problem 26: Laptop Purchase EMI Definition Nested if-else statements help decide 
# the payment option based on product price. Task Read laptop price and whether 
# the customer selected EMI. If the laptop price is greater than ₹50000:
#  If EMI is selected, offer EMI payment. Otherwise, print Pay Full Amount. 
# Otherwise, print EMI Not Available for This Price. 
# Example Input Laptop Price: 65000 
# EMI Selected: True Example
#  Output EMI Approved 

price = int(input("Laptop Price: "))
if price>50000:
    is_emi = input("EMI Selected: ")
    if is_emi.lower()=='true':
        print("EMI Approved")
    else:
        print("Pay Full Amount")
else:
    print("EMI Not available for this price")

'''
Output:
Laptop Price: 65000
EMI Selected: True
EMI Approved
'''

# Problem 27: School Bus Service Definition Nested conditions verify fee payment 
# before checking the bus pass. Task Read fee payment status and bus pass availability.
# If fees are paid: If the student has a bus pass, 
# alow boarding. Otherwise, print Collect Bus Pass. Otherwise,
#  print Pay School Fees First. 
# Example Input Fees Paid: True
#  Bus Pass Available: True 
# Example Output Boarding Alowed 

fee_paid = input("Fees Paid: ")
if fee_paid.lower()=='true':
    bus_pass = input("Bus Pass Available: ")
    if bus_pass.lower()=='true':
        print("Boarding Allowed")
    else:
        print("Collect Bus Pass")
else:
    print("Pay School Fees First")

'''
Output:
Fees Paid: True
Bus Pass Available: True
Boarding Allowed
'''

# Problem 28: Petrol Pump Definition Nested conditions ensure fuel is available
# before processing payment. Task Read fuel availability and payment status. 
# If fuel is available: If payment is successful, fi l the fuel. Otherwise, 
# print Payment Failed. Otherwise, print Fuel Not Available. 
# Example Input Fuel Available: True 
# Payment Successful: True 
# Example Output Fuel Fi led Successfu ly 

fuel = input("Fuel Available: ")
if fuel.lower()=='true':
    payment=input("Payment Successful: ")
    if payment.lower()=='true':
        print("Fuel Filled Successfully")
    else:
        print("Payment Failed")
else:
    print("Fuel Not Available")

'''
Output:
Fuel Available: True
Payment Successful: True
Fuel Filled Successfully
'''

# Problem 29: Warehouse Entry Definition Nested if-else statements are commonly used 
# for security verification. Task Read ID card availability and fingerprint verification
#  status. If the employee has an ID card: If the fingerprint is verified, a low entry.
#  Otherwise, print Fingerprint Verification Failed. Otherwise, 
# print ID Card Required.
#  Example Input ID Card Available: True 
# Fingerprint Verified: True 
# Example Output Entry Alowed

id_card = input("ID Card Available: ")
if id_card.lower()=='true':
    fingerprint = input("Fingerprint Verified: ")
    if fingerprint.lower()=='true':
        print("Entry Allowed")
    else:
        print("Fingerprint Verification Failed")
else:
    print("ID Card Required")

'''
Output:
ID Card Available: True
Fingerprint Verified: True
Entry Allowed
'''


# Problem 30: Software Installation Definition Nested conditions help 
# verify system requirements before insta ling software. 
# Task Read operating system compatibility and available storage. 
# If the operating system is compatible: If available storage is at least 20 GB, 
# insta l the software. Otherwise, print Insufficient Storage. 
# Otherwise, print Operating System Not Supported. 
# Example Input Operating System Compatible: True 
# Available Storage: 50 
# Example Output Software Instaled Successfuly 

Os_Compatible = input("Operating System Compatible: ")
if Os_Compatible.lower()=='true':
    storage = int(input("Available Storage:"))
    if storage>=20:
        print("Software Installed Successfully")
    else:
        print("Insufficient Storage")
else:
    print("Operating System Not Supported")

'''
Output:
Operating System Compatible: True
Available Storage:52
Software Installed Successfully
'''
