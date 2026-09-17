 
# Part 1: 15 Real-Time Problems on for loop 
# with else 
 
# 1. ATM Withdrawal Validation 
# Concept: 
# Use for-else to check whether the ATM has enough notes to 
# process a withdrawal. 
# Task: 
# An ATM has available note denominations. Check whether the 
# requested amount can be formed using available notes. If no 
# combination is possible, execute else. 
# Example Input: 
# 5 
# 100 200 500 1000 2000 
# 150 
 
# Example Output: 
# Withdrawal cannot be processed 

n = int(input("Enter how many notes in ATM: "))

notes = []

for i in range(n):
    note = int(input("Enter the notes: "))
    notes.append(note)

money = int(input("Enter the withdraw money: "))

for comb in range(1, 2 ** n):
    current_sum = 0
    for i in range(n):
        if comb & (1 << i):
            current_sum += notes[i]

    if current_sum == money:
        print("Withdraw can be processed")
        break
else:
    print("Withdraw cannot be processed")

'''
Output:
Enter how many notes in ATM: 5 
Enter the notes: 100
Enter the notes: 200
Enter the notes: 500
Enter the notes: 1000
Enter the notes: 2000
Enter the withdraw money: 150
Withdraw cannot be processed
'''   

 
# 2. Detect Fraud Transaction 
# Task: 
# A bank system checks transactions. If any transaction crosses 
# the fraud limit, stop checking. 
# Example Input: 
# 6 
# 5000 12000 3000 25000 4000 7000 
# 10000 
 
# Example Output: 
# Suspicious transaction detected 
 
n = int(input("Enter how many transactions: "))
trans = []
for ele in range(n):
    money = int(input("Enter the transaction: "))
    trans.append(money)
limit = int(input("Enter the fraud limit: "))
for i in range(len(trans)):
    if trans[i]>=limit:
        print("Suspicious transaction detected")
        break
else:
    print(f'No Suspicious transaction detected')

'''
Output:
Enter how many transactions: 6
Enter the transaction: 5000
Enter the transaction: 12000
Enter the transaction: 3000
Enter the transaction: 25000
Enter the transaction: 4000
Enter the transaction: 7000
Enter the fraud limit: 10000
Suspicious transaction detected
'''


 
# 3. Validate Student Marks Entry 
# Task: 
# Check whether all entered marks are valid (0 to 100). If an invalid 
# mark is found, stop checking. 
# Example Input: 
# 5 
# 78 85 92 110 65 
# Example Output: 
# Invalid marks found 
 
 
n = int(input("Enter how many students marks: "))
marks=[]
for i in range(1,n+1):
    mark = int(input(f"Enter the student {i} marks: "))
    marks.append(mark)
for mark in marks:
    if mark<0 or mark>=100:
        print("Invalid marks is found")
        break
else:
    print("Marks validation successful")

'''
Enter how many students marks: 5
Enter the student 1 marks: 78
Enter the student 2 marks: 85
Enter the student 3 marks: 92
Enter the student 4 marks: 110
Enter the student 5 marks: 65
Invalid marks is found
'''

 
# 4. Find Available Parking Slot 
# Task: 
# A parking system checks slots one by one. Find the first empty 
# slot. 
# (0 = empty, 1 = occupied) 
# Example Input: 
# 6 
# 1 1 1 0 1 0 
# Example Output: 
# Parking slot available 
 
n = int(input("Enter how many slots: "))
parking = []
for i in range(1,n+1):
    slot = int(input("Enter the slot (0 = empty, 1 = occupied): "))
    parking.append(slot)
for slot in parking:
    if slot == 0:
        print("Parking Slot Available")
        break
else:
    print("Parking slots are not Available")

'''
Output:
Enter how many slots: 6
Enter the slot (0 = empty, 1 = occupied): 1
Enter the slot (0 = empty, 1 = occupied): 1
Enter the slot (0 = empty, 1 = occupied): 1
Enter the slot (0 = empty, 1 = occupied): 0
Enter the slot (0 = empty, 1 = occupied): 1
Enter the slot (0 = empty, 1 = occupied): 0
Parking Slot Available
'''

 
 
# 5. Check Product Quality 
# Task: 
# A factory checks product quality scores. If any product score is 
# below the minimum quality level, reject the batch. 
# Example Input: 
# 5 
# 90 85 76 40 95 
# 50     
# Example Output: 
# Quality check failed 

n = int(input("Enter how many quality scores stored: "))
quaScores = []
for i in range(1,n+1):
    score = int(input(f"Enter the product {i} quality score: "))
    quaScores.append(score)
checkScore = int(input("Enter the minimum quality score:"))
for score in quaScores:
    if score<checkScore:
        print('Quality Check Failed')
        break
else:
    print("Quality check sucessful")


'''
Output:
Enter how many quality scores stored: 5
Enter the product 1 quality score: 90
Enter the product 2 quality score: 85
Enter the product 3 quality score: 76
Enter the product 4 quality score: 40
Enter the product 5 quality score: 95
Enter the minimum quality score:50
Quality Check Failed
'''
 
 
# 6. Verify Password Rules 
# Task: 
# Check whether a password contains at least one uppercase 
# letter. 
# Example Input: 
# welcome123 
# Example Output: 
# Password does not contain uppercase letter 

pword = input("Enter the password: ")
for word in pword:
    if word.isupper():
        print("Password contain uppercase letter")
        break
else:
    print('Password does not contain uppercase letter')

'''
Output:
Enter the password: welcome123
Password does not contain uppercase letter
'''


# 7. Find Available Doctor Appointment 
# Task: 
# Check doctor slots. Find whether any slot is available. 
# (1 = booked, 0 = available) 
# Example Input: 
# 5 
# 1 1 0 1 1 
# Example Output: 
# Appointment available 

n = int(input("Enter how many appointment are : "))
appMents = []
for i in range(1,n+1):
    book = int(input("Enter the slot (1 = booked, 0 = available): "))
    appMents.append(book)
for num in appMents:
    if num == 0:
        print("Appointment available")

'''
Output:
Enter how many appointment are : 5
Enter the slot (1 = booked, 0 = available): 1
Enter the slot (1 = booked, 0 = available): 1
Enter the slot (1 = booked, 0 = available): 0
Enter the slot (1 = booked, 0 = available): 1
Enter the slot (1 = booked, 0 = available): 1
Appointment available
'''



# 8. Detect Damaged Packages 
# Task: 
# A courier company checks package weights. If weight is less than 
# 1 kg, mark as damaged. 
# Example Input: 
# 5 
# 2.5 3.0 0.5 4.0 1.8 
# Example Output: 
# Damaged package found 

n = int(input("Enter how many weights in courier: "))
weights = []
for i in range(1,n+1):
    weight = float(input(f"Enter the weight {i}: "))
    weights.append(weight)

for weight in weights:
    if weight<1:
        print("Damage package found")
        break
else:
    print('All weights are ok')

'''
Output:
Enter how many weights in courier: 5
Enter the weight 1: 2.5
Enter the weight 2: 3
Enter the weight 3: 0.5
Enter the weight 4: 4
Enter the weight 5: 1.8
Damage package found
'''


# 9. Check Password Attempts History 
# Task: 
# Check previous login attempts. If a successful login exists, stop 
# checking. 
# (1 = success, 0 = failure) 
# Example Input: 
# 6 
# 0 0 0 1 0 0 
# Example Output: 
# Successful login found 

n = int(input("Enter how many login attempts do: "))
logins= []
for i in range(1,n+1):
    attempt = int(input(f"Enter the login {i} attempt (1 = success, 0 = failure) : "))
    logins.append(attempt)

for attem in logins:
    if attem == 1:
        print("Successful login found")
        break
else:
    print("Login not found")

'''
Output:
Enter how many login attempts do: 6
Enter the login 1 attempt (1 = success, 0 = failure) : 0
Enter the login 2 attempt (1 = success, 0 = failure) : 0
Enter the login 3 attempt (1 = success, 0 = failure) : 0
Enter the login 4 attempt (1 = success, 0 = failure) : 1
Enter the login 5 attempt (1 = success, 0 = failure) : 0
Enter the login 6 attempt (1 = success, 0 = failure) : 0
Successful login found
'''




# 10. Check Library Book Condition 
# Task: 
# Check returned books. If any book is damaged, report it. 
# (0 = good, 1 = damaged) 
# Example Input: 
# 5 
# 0 0 0 1 0 
# Example Output: 
# Damaged book detected 

n = int(input("Enter how many books checked: "))
books = []
for i in range(1,n+1):
    checkBook = int(input("Enter the book condition (0 = good, 1 = damaged): "))
    books.append(checkBook)

for book in books:
    if book == 1:
        print("Damaged book detected")
        break
else:
    print("No Damage book found")


'''
Output:
Enter how many books checked: 5
Enter the book condition (0 = good, 1 = damaged): 0
Enter the book condition (0 = good, 1 = damaged): 0
Enter the book condition (0 = good, 1 = damaged): 0
Enter the book condition (0 = good, 1 = damaged): 1
Enter the book condition (0 = good, 1 = damaged): 0
Damaged book detected`
'''


# 11. Find Nearest Charging Station 
# Task: 
# Check distances of charging stations. Find if a station exists 
# within 5 km. 
# Example Input: 
# 6 
# 12 8 10 4 15 20 
# Example Output: 
# Charging station found 

n = int(input("Enter how many charging stations distance: "))
chStations = []
for i in range(1,n+1):
    dis = int(input(f"Enter the distance of station {i}: "))
    chStations.append(dis)
for distance in chStations:
    if distance<=5:
        print("Charging station is found")
        break
else:
    print("Charging station not found near by distance")

'''
Output:
Enter how many charging stations distance: 6
Enter the distance of station 1: 12
Enter the distance of station 2: 8
Enter the distance of station 3: 10
Enter the distance of station 4: 4
Enter the distance of station 5: 15
Enter the distance of station 6: 20
Charging station is found
'''

# 12. Check Website Server Status 
# Task: 
# A monitoring system checks servers. If any server is active, stop 
# checking. 
# (1 = active, 0 = down) 
# Example Input: 
# 5 
# 0 0 1 0 0 
# Example Output: 
# Active server found 
 
n = int(input("Enter how many servers status in the list: "))
status = []
for i in range(1,n+1):
    s = int(input(f"Enter the status of server {i}(1 = active, 0 = down) : "))
    status.append(s)

for st in status:
    if st == 1:
        print("Active server found")
        break
else:
    print('No active servers found')

'''
Output:
Enter how many servers status in the list: 5
Enter the status of server 1(1 = active, 0 = down) : 0
Enter the status of server 2(1 = active, 0 = down) : 0
Enter the status of server 3(1 = active, 0 = down) : 1
Enter the status of server 4(1 = active, 0 = down) : 0
Enter the status of server 5(1 = active, 0 = down) : 0
Active server found
'''

 
# 13. Verify Attendance Records 
# Task: 
# Check attendance percentage of students. If any student 
# attendance is below 75%, stop checking. 
# Example Input: 
# 5 
# 90 85 76 60 88 
# 75  
# Example Output: 
# Attendance shortage detected 
 
n = int(input("Enter how many students check for attendence: "))
attd = []
for i in range(1,n+1):
    a = int(input(f"Enter the attendence percentage of student {i}: "))
    attd.append(a)  
per = int(input("Enter the limit of attendence: ")) 
for num in attd:
    if num<per:
        print("Attendence shortage detected")
        break
else:
    print("Attendence shortage not detected")

'''
Output:
Enter how many students check for attendence: 5
Enter the attendence percentage of student 1: 90
Enter the attendence percentage of student 2: 85
Enter the attendence percentage of student 3: 76
Enter the attendence percentage of student 4: 60
Enter the attendence percentage of student 5: 88
Enter the limit of attendence: 75
Attendence shortage detected
'''


# 14. Detect Duplicate Booking 
# Task: 
# Check booking IDs. If duplicate booking ID appears, stop. 
# Example Input: 
# 6 
# 101 205 303 205 404 505 
# Example Output: 
# Duplicate booking found 

n = int(input("Enter how many booking ids check: "))
bookIds = []
for i in range(1,n+1):
    id = int(input("Enter the booking id: "))
    bookIds.append(id)
for i in range(len(bookIds)-1):
    found = False
    for j in range(i+1,len(bookIds)):
        if bookIds[i]==bookIds[j]:
            print("Duplicate booking Found")
            found = True
            break
    if found:
        break
else:
    print("Duplicate booking not found")

'''
Output:
Enter how many booking ids check: 6
Enter the booking id: 101
Enter the booking id: 205
Enter the booking id: 303
Enter the booking id: 205
Enter the booking id: 404
Enter the booking id: 505
Duplicate booking Found
'''



# 15. Check Security Access Cards 
# Task: 
# Check access card status. If an expired card is found, deny entry. 
# (1 = valid, 0 = expired) 
# Example Input: 
# 5 
# 1 1 0 1 1 
# Example Output: 
# Expired card detected 

n = int(input("Enter how many cards status in the list: "))
status = []
for i in range(1,n+1):
    s = int(input(f"Enter the status of the card {i} (1 = valid, 0 = expired): "))
    status.append(s)

for s in status:
    if s==0:
        print("Expired card detected")
        break
else:
    print("No Expired cards")

'''
Output:
Enter how many cards status in the list: 5
Enter the status of the card 1 (1 = valid, 0 = expired): 1
Enter the status of the card 2 (1 = valid, 0 = expired): 1
Enter the status of the card 3 (1 = valid, 0 = expired): 0
Enter the status of the card 4 (1 = valid, 0 = expired): 1
Enter the status of the card 5 (1 = valid, 0 = expired): 1
Expired card detected
'''

# Part 2: 15 Real-Time Problems on while 
# loop with else 
# 1. ATM PIN Verification System 
# Concept: 
# The ATM allows limited attempts. If the correct PIN is entered, 
# stop using break. If all attempts finish, execute else. 
# Task: 
# Allow 3 attempts to enter the correct PIN. 
# Example Input: 
# 1234 
# 3 
# 5678 
# 1111 
# 9999 
 
# Example Output: 
# Account blocked 
 
password = input("Enter the main password: ")
attempts = int(input("Enter how many attempts to check the password: "))
i = 1
while i<=attempts:
    user_pd = input("Enter the password: ")
    if user_pd==password:
        print("Withdraw successful")
        break
    i+=1
else:
    print("Account blocked")

'''
Output:
Enter the main password: 1234
Enter how many attempts to check the password: 3
Enter the password: 5678
Enter the password: 1111
Enter the password: 9999
Account blocked
'''
 
# 2. Online Payment Retry System 
# Task: 
# A payment system retries payment until it succeeds or maximum 
# attempts are completed. 
# (1 = success, 0 = failure) 
# Example Input: 
# 4 
# 0 
# 0 
# 0 
# 0 
 
# Example Output: 
# Payment failed after retries 
 
n = int(input("Enter how many attempts: "))
payment_status = []
i = 1
while i<=n:
    pay = int(input("Enter the status of payment (1 = success, 0 = failure): " ))
    if pay == 1:
        print("Payment Successful")
        break
    i+=1
else:
    print("Payment failed after retries")

'''
Output:
Enter how many attempts: 4
Enter the status of payment (1 = success, 0 = failure): 0
Enter the status of payment (1 = success, 0 = failure): 0
Enter the status of payment (1 = success, 0 = failure): 0
Enter the status of payment (1 = success, 0 = failure): 0
Payment failed after retries
'''
 
# 3. OTP Verification 
# Task: 
# Allow user 3 attempts to enter the correct OTP. 
# Example Input: 
# Correct OTP: 7890 
 
# Attempts: 
# 1234 
# 5678 
# 7890 
 
# Example Output: 
# OTP verified successfully 
 
OTP = int(input("Enter the correct OTP: "))
i = 1
while i<=3:
    user_otp = int(input("Enter the OTP: "))
    if user_otp == OTP:
        print("OTP verified successfully")
        break
    i+=1
else:
    print("No attempts to enter otp")

'''
Output:
Enter the correct OTP: 7890
Enter the OTP: 1234
Enter the OTP: 5678
Enter the OTP: 7890
OTP verified successfully
'''
 
# 4. File Download Retry 
# Task: 
# A file download system tries downloading until successful. 
# (1 = download success, 0 = failed) 
# Example Input: 
# 5 
# 0 
# 0 
# 1 
 
# Example Output: 
# File downloaded successfully 
 
n = int(input("Enter how many tries to download the file: "))
i = 1
while i<=n:
    status = int(input("Enter the status of downloading file (1 = download success, 0 = failed):"))
    if status == 1:
        print("File downloaded successfully")
        break
    i+=1
else:
    print("File Download Retry")

'''
Output:
Enter how many tries to download the file: 5
Enter the status of downloading file (1 = download success, 0 = failed):0
Enter the status of downloading file (1 = download success, 0 = failed):0
Enter the status of downloading file (1 = download success, 0 = failed):1
File downloaded successfully
'''

 
# 5. Game Life System 
# Task: 
# A player gets 3 chances. Continue playing until lives become 
# zero. 
# Example Input: 
# 3 
# 1 
# 1 
# 1 
 
# (1 means life lost) 
# Example Output: 
# Game over 

chances = int(input("Enter how many chances we have: "))
while chances>0:
    c = int(input("Enter the lives (1 means life lost) zero means nothing: "))
    if c==1:
        chances-=1
else:
    print("Game Over")

'''
Output:
Enter how many chances we have: 3
Enter the lives (1 means life lost) zero means nothing: 1
Enter the lives (1 means life lost) zero means nothing: 1
Enter the lives (1 means life lost) zero means nothing: 1
Game Over
'''

# 6. Battery Charging System 
# Task: 
# Increase battery level by 10% until it reaches 100%. 
# Example Input: 
# 70 
# Example Output: 
# Battery fuly charged 

battery = int(input("Enter the charge percentage of battery: "))
while battery<=100:
    battery+=10
    if battery == 100:
      print("Battery Full charged")
      break
else:
    print("Battery not Fully charged")

'''
Output:
Enter the charge percentage of battery: 70
Battery Fully charged
'''

# 7. Elevator Movement System 
# Task: 
# Move an elevator floor by floor until it reaches the destination. 
# Example Input: 
# Current floor: 2 
# Destination floor: 6 
# Example Output: 
# Reached destination floor

curr_floor = int(input("Current floor: "))
dest_floor = int(input("Destination floor: "))

while curr_floor<=dest_floor:
    curr_floor+=1
    if curr_floor==dest_floor:
        print("Reached destination floor")
        break
else:
    print("Not Reached destination floor")

'''
Output:
Current floor: 2
Destination floor: 6
Reached destination floor
'''

# 8. Traffic Signal Countdown 
# Task: 
# Decrease signal timer until it reaches zero. 
# Example Input: 
# 5 
 
# Example Output: 
# Signal changed 

n = int(input("Enter the timer: "))
while n>=0:
    n-=1
    if n==0:
        print("Signal changed")
        break
else:
    print("Signal not changed")

'''
Output:
Enter the timer: 5
Signal changed
'''
 
# 9. Server Restart System 
# Task: 
# A server tries restarting 3 times. If it starts, stop retrying. 
# (1 = started, 0 = failed) 
# Example Input: 
# 3 
# 0 
# 0 
# 0 
 
# Example Output: 
# Server restart failed 
 
times = int(input("Enter how many times to try: "))
while times>0:
    status = int(input("Enter the status of server (1 = started, 0 = failed): "))
    if status==1:
        print("Server restarted suceessful")
        break
    times-=1
else:
    print("Server restart failed")

'''
Output:
thon/Exan2/RealTime15forLoop.py
Enter how many times to try: 3
Enter the status of server (1 = started, 0 = failed): 0
Enter the status of server (1 = started, 0 = failed): 0
Enter the status of server (1 = started, 0 = failed): 0
Server restart failed
'''

# 10. Food Delivery Tracking 
# Task: 
# Check order status until delivery is completed. 
# (0 = not delivered, 1 = delivered) 
# Example Input: 
# 4 
# 0 
# 0 
# 0 
# 1 
 
# Example Output: 
# Order delivered 
 
times = int(input("Enter how many attempts to check: "))
while times>0:
     s = int(input("Enter the status of delivery (0 = not delivered, 1 = delivered): "))
     if s==1:
          print("Order delivered")
          break
else:
     print('Order delivery failed')

'''
Output:
Enter how many attempts to check: 4
Enter the status of delivery (0 = not delivered, 1 = delivered): 0
Enter the status of delivery (0 = not delivered, 1 = delivered): 0
Enter the status of delivery (0 = not delivered, 1 = delivered): 0
Enter the status of delivery (0 = not delivered, 1 = delivered): 1
Order delivered
'''

# 11. Internet Connection Retry 
# Task: 
# A device tries connecting to the internet. 
# (1 = connected, 0 = failed) 
# Example Input: 
# 5 
# 0 
# 0 
# 0 
# 0 
# 0 
 
# Example Output: 
# Unable to connect 
 
n = int(input("Enter how many times to try: "))
while n>0:
    conn = int(input("Enter the status of internet connection 1 or 0: "))
    if conn==1:
        print("A device internet connection successful")
        break
    n-=1
else:
    print("Unable to connect")

'''
Output:
Enter how many times to try: 5
Enter the status of internet connection 1 or 0: 0
Enter the status of internet connection 1 or 0: 0
Enter the status of internet connection 1 or 0: 0
Enter the status of internet connection 1 or 0: 0
Enter the status of internet connection 1 or 0: 0
Unable to connect
'''


# 12. Password Reset Verification 
# Task: 
# A user gets limited attempts to verify identity. 
# (1 = verified, 0 = failed) 
# Example Input: 
# 3 
# 0 
# 1 
 
# Example Output: 
# Identity verified 

attempts = int(input("Enter how many attempts to verify: "))
while attempts>0:
    ver = int(input("Enter the verify of identity 1 or 0: "))
    if ver == 1:
        print("Identity verified")
        break
else:
    print("Identity not verified")

'''
Output:
Enter how many attempts to verify: 3
Enter the verify of identity 1 or 0: 0
Enter the verify of identity 1 or 0: 1
Identity verified
'''

 
# 13. Washing Machine Cycle 
# Task: 
# Reduce remaining time until washing completes. 
# Example Input: 
# 30 
 
# Example Output: 
# Washing completed 

time = int(input("Enter how much time to complete washing: "))

while time>0:
    time-=1
    if time==0:
        print("Washing completed")
        break
else:
    print("Washing not completed")

'''
Output:
Enter how much time to complete washing: 30
Washing completed
'''

# 14. Inventory Restocking System 
# Task: 
# Increase stock quantity until required stock level is reached. 
# Example Input: 
# Current stock: 
# 40 
 
# Required stock: 
# 100 
 
# Example Output: 
# Stock requirement completed 
 
curr_stock = int(input("Current stock: "))
req_stock = int(input("Required stock: "))
while curr_stock<=req_stock:
    curr_stock+=1
    if curr_stock == req_stock:
        print("Stock requirement completed")
        break
else:
    print("Stock requirement not completed")

'''
Output:
Current stock: 40
Required stock: 100
Stock requirement completed
'''
 
# 15. Bank Transaction Processing Queue 
# Task: 
# Process transactions one by one until all are completed. 
# (1 = completed, 0 = failed) 
# Example Input: 
# 5 
# 1 
# 1 
# 1 
# 1 
# 1 
 
# Example Output: 
# All transactions processed

trans = int(input("Enter how many transactions processed: "))

while trans>0:
    status = int(input("Enter the status of transaction 1 or 0: "))
    if status==0:
        print("Transaction process failed")
        break
    trans-=1
else:
    print("All transactions processed")

'''
Output:
Enter how many transactions processed: 5
Enter the status of transaction 1 or 0: 1
Enter the status of transaction 1 or 0: 1
Enter the status of transaction 1 or 0: 1
Enter the status of transaction 1 or 0: 1
Enter the status of transaction 1 or 0: 1
All transactions processed
'''


