# 1. Find First Failed Temperature Definition:
# A weather-monitoring system checks temperatures recorded during the day. 
# Task: Read n temperature values. If any temperature is below 0, 
# stop checking immediately using break
# and display that the first freezing temperature was found. 
# If no temperature is below 0, use loop else to display that all temperatures were safe. 
# Example Input: 5 12 18 21 15 9
# Example Output: No freezing temperature found
n = int(input("Enter the size: "))
temps = []
for i in range(n):
    temp = int(input("Enter the temperature: "))
    temps += [temp]
i = 0
while i<len(temps):
    if temps[i]<0:
        print(f"The first freezing temperature {temps[i]} celsius found")
        break
    i+=1
else:
    print("No freezing temperature found")

'''
Output:
Enter the size: 5
Enter the temperature: 12
Enter the temperature: 18
Enter the temperature: 21
Enter the temperature: 15
Enter the temperature: 9
No freezing temperature found
'''




# 2. ATM PIN Verification Definition: An ATM allows a user a maximum of 3 attempts 
# to enter the correct PIN. 
# Task: Keep asking for the PIN using a loop. If the correct PIN is entered, 
# use break and display Access Granted. If all 3 attempts fail, 
# use loop else to display Card Blocked. 
# Example Input: 
# 1111 
# 2222 
# 1234 
# Example Output: Access Granted

pin = 1234
attempts = 1
while attempts<=3:
    user_pin = input("Enter the ATM Pin: ")
    if int(user_pin) == pin:
        print("Access Granted")
        break
    attempts+=1
else:
    print("Card Blocked")

'''
Output:
Enter the ATM Pin: 1232
Enter the ATM Pin: 2342
Enter the ATM Pin: 1234
Access Granted
'''

# 3. Search for a Product Definition: A shopping application stores product IDs.
# Task: Read n product IDs and then search for a given product ID.
# Stop the loop using break when the product is found. 
# If the loop completes without finding it, use else. 
# Example Input: 6
# 101 205 310 415 520 625 
# 415
# Example Output: Product found

productsIds = []
n = int(input("Enter the size: "))
for i in range(n):
    prod_id = int(input("Enter the product Id: "))
    productsIds +=[prod_id]
search = int(input("Enter the search product Id: "))
for ids in productsIds:
    if ids == search:
        print("Product found")
        break
else:
    print("Product Not Found")

'''
Output:
Enter the size: 6
Enter the product Id: 101
Enter the product Id: 205
Enter the product Id: 310
Enter the product Id: 415
Enter the product Id: 520
Enter the product Id: 625
Enter the search product Id: 415
Product found
'''

# 4. First Divisible Number Definition: A number-monitoring system needs to find the first number 
# in a range that is divisible by both 7 and 9.
# Task: Read two numbers representing the starting and ending values. 
# Check every number using a loop. Stop at the first number divisible by both.
# Example Input: 100 200
# Example Output: 
# First matching number: 126
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
while start<=end:
    if start%7 == 0 and start%9 == 0:
        print(f'First matching number: {start}')
        break
    start+=1
else:
    print("There is no values")

'''
Output:
Enter the start number: 100
Enter the end number: 200
First matching number: 126

'''

# 5. Parking Slot Search Definition: A parking area has slots represented by 
# 0 for Empty and 1 for Occupied. Task: Read the status of n parking slots. 
# Find the first empty slot. Stop using break. If every slot is occupied, use loop else.
# Example Input: 6
#  1 1 1 0 1 0 
# Example Output: First empty slot: 4
n = int(input("Enter the size: "))
park_slots=[]
for i in range(n):
    slot = int(input("Enter the 0 or 1 : "))
    park_slots+=[slot]
i = 0
while i<n:
    if not park_slots[i]:
        print(f"First Empty slot: {i+1}")
        break
    i+=1
else:
    print("The slots are not available")

'''
Output:
Enter the size: 6
Enter the 0 or 1 : 1
Enter the 0 or 1 : 1
Enter the 0 or 1 : 1
Enter the 0 or 1 : 0
Enter the 0 or 1 : 1
Enter the 0 or 1 : 0
First Empty slot: 4
'''


# 6. Detect Negative Transaction Definition: A financial system records daily transaction amounts. 
# Task: Read n transaction values. If a negative transaction is encountered, stop immediately and 
# display its position and value. If there are no negative transactions, use loop else. 
# Example Input: 5 
# 1200 850 430 -200 900 
# Example Output: Negative transaction found at position 4: -200

n = int(input("Enter the size: "))
trans = []
for i in range(n):
    amount = int(input("Enter the amount: "))
    trans += [amount]

i = 0
while i<n:
    if trans[i]<0:
        print(f'Negative Transaction found at position {i+1}: {trans[i]}')
        break
    i+=1
else:
    print("there is no negative transactions")

'''
Output: 
Enter the size: 5
Enter the amount: 1200
Enter the amount: 850
Enter the amount: 430
Enter the amount: -200
Enter the amount: 900
Negative Transaction found at position 4: -200
'''


# 7. Find First Prime Number Definition: A system receives numbers one by one and wants 
# to find the first prime number.Task: Read n numbers. For each number, check whether
# it is prime using a loop. As soon as the first prime is found, stop searching using break. 
# If no prime exists, use loop else. 
# Example Input: 5 
# 21 27 35 41 49 
# Example Output: First prime number: 41

n = int(input("Enter the size: "))
nums = []
for i in range(n):
    num = int(input("Enter the amount: "))
    nums += [num]
i = 0
while i<n:
    if nums[i]>1:
        for j in range(2,int(nums[i]**0.5)+1):
            if nums[i]%j==0:
                break
        else:
            print(f"First prime number : {nums[i]}")
            break
    i+=1
else:
    print(f'There is no prime numbers')

'''
Output:
Enter the size: 5
Enter the amount: 21
Enter the amount: 27
Enter the amount: 35
Enter the amount: 41
Enter the amount: 49
First prime number : 41
'''

# 8. Password Strength Checking Definition: A registration system checks whether a password contains
# at least one digit. Task: Read a password character by character using a loop. 
# If a digit is found, stop using break. If no digit is found after checking the entire password, 
# use loop else.
# Example Input: python@code 
# Example Output: Password must contain a digit

password = input("Enter the password: ")
contain_nums = '0123456789'
for char in password:
    if char in contain_nums:
        print("Password is strong")
        break
else:
    print("Password must contain a digit")

'''
Output:
Enter the password: python@code
Password must contain a digit
'''

# 9. Find First Number Above Limit Definition: A sensor records water levels. 
# Task: Read n water-level readings and a danger limit. Find the first reading greater than the danger limit. 
# Stop immediately using break. If none exceeds the limit, use loop else. 
# Example Input: 5 80 65 72 78 85 91
# Example Output: Danger level detected: 85

n = int(input("Enter the size: "))
danger = int(input("Enter the limit: "))
levels = []
for i in range(n):
    ele = int(input("Enter the number level: "))
    levels +=[ele]
i = 0
while i < n:
    if levels[i]>danger:
        print(f"Danger level detected : {levels[i]}")
        break
    i+=1
else:
    print("There is no values in above the limit")


'''
Output:
Enter the size: 5
Enter the limit: 80
Enter the number level: 65
Enter the number level: 72
Enter the number level: 78
Enter the number level: 85
Enter the number level: 91
Danger level detected : 85
'''


# 10. Shopping Budget Checker Definition: A customer enters the prices of items one by one.
# Task: Read the customer's budget and item prices. Keep calculating the total. 
# If the total exceeds the budget,
# stop using break. If all items are processed without exceeding the budget, use loop else.
# Example Input: 1000 5 200 150 180 120 100
# Example Output: Purchase completed Total: 750
budget = int(input("Enter the Budget: "))
size = int(input("Enter the size: "))
prices = []
for i in range(size):
    item_price = int(input("Enter the price: "))
    prices+=[item_price]
i=0
total = 0
while i<size:
    total+=prices[i]
    if total>budget:
        print("total exceeds the budget")
        break
    i+=1
else:
    print(f'Purchase completed Total: {total}')

'''
Output:
Enter the Budget: 1000
Enter the size: 5
Enter the price: 200
Enter the price: 150
Enter the price: 180
Enter the price: 120
Enter the price: 100
Purchase completed Total: 750
'''


# 11. Find First Repeated Number Definition:
# A system receives a sequence of numbers and wants to detect whether
# any number appears twice. Task: Check each number against the numbers
# that appeared before it. When a repeated number is found, stop using break. 
# If no repetition exists, use loop else.
# Example Input: 6 
# 12 25 18 34 25 40 
# Example Output: Repeated number found: 25
size = int(input("Enter the size: "))
nums = []
for i in range(size):
    num = int(input("Enter the number: "))
    nums += [num]
i=0
found = False
while i<size:
    j = i+1
    while j<size-1:
        if nums[i]==nums[j]:
            print(f'Repeated number found: {nums[i]}')
            found = True
            break
        j+=1
    if found:
        break
    i+=1
else:
    print(" No repeated numbers in the list")


'''
Output:
Enter the size: 6
Enter the number: 12
Enter the number: 25
Enter the number: 18
Enter the number: 34
Enter the number: 25
Enter the number: 40
Repeated number found: 25
'''


# 12. Exam Pass Checker Definition: A student has marks from multiple subjects.
# Task: Read marks for n subjects. If any subject mark is below 35, stop checking using break and 
# display Failed. If every subject is passed, use loop else to display Passed.
#    Example Input: 5 
# 72 65 81 29 90 
# Example Output: Failed Failed subject mark: 29
size = int(input("Enter how many subjects: "))
marks = []
for i in range(size):
    mark = int(input("Enter the marks: "))
    marks +=[mark]
i = 0
while i < size:
    if marks[i]<35:
        print(f"Failed, Failed subject marks is {marks[i]}")
        break
    i+=1
else:
    print("passed all subjects")


'''
Output:
Enter how many subjects: 5
Enter the marks: 72
Enter the marks: 65
Enter the marks: 81
Enter the marks: 29
Enter the marks: 90
Failed, Failed subject marks is 29
'''


# 13. Find First Perfect Square Definition: 
# A mathematical application receives a range of numbers. 
# Task: Check every number in the range and find the first number whose square root is an exact integer. 
# Stop using break. If no perfect square exists, use loop else. 
# Example Input: 10 30 Example Output: First perfect square: 16

start = int(input("Enter the starting number: "))
end = int(input("Enter the end number: "))
found = False
while start<=end:
    for num in range(start):
        if num*num == start:
            print(f"First perfect square: {start}")
            found = True
            break
    if found:
        break
    start+=1
else:
    print(f"There is no perfect square numbers between {start} to {end}")

'''
Output:
Enter the starting number: 10
Enter the end number: 30
First perfect square: 16
'''

# 14. Delivery Weight Checker Definition: A delivery company checks packages one by one. 
# Task: Read the maximum allowed weight and the weights of n packages.
# If a package exceeds the limit, stop using break and display its package number.
# If every package is within the limit, use loop else
# . Example Input: 
# 10
# 5 4 7 8 12 6 
# Example Output: Package 4 exceeds the limit: 12 kg
weight = int(input("Enter the limit_weight: "))
package_size = int(input("Enter the size of the package: "))
packages=[]
for i in range(package_size):
    pack_weight = int(input("Enter the pack weight: "))
    packages +=[pack_weight]
i = 0
while i<package_size:
    if packages[i]>weight:
        print(f'package {i+1} exceeds the limit: {packages[i]} kg')
        break
    i+=1
else:
    print("all package weights are under the limit")


'''
Output: 
Enter the limit_weight: 10
Enter the size of the package: 5
Enter the pack weight: 4
Enter the pack weight: 7
Enter the pack weight: 8
Enter the pack weight: 12
Enter the pack weight: 6
package 4 exceeds the limit: 12 kg
'''

# 15.Find First Number with Digit Sum 10
#  Definition: A number-processing system needs to find the first number whose sum of digits
#  is exactly 10. Task: Read n numbers. For each number, calculate its digit sum using a loop. 
#  If the digit sum is 10, stop searching using break. If no such number exists, 
# use the outer loop's else. 
# Example Input: 5 
# 123 245 341 562 901 
# Example Output: First matching number: 245
size = int(input("Enter the size: "))
nums = []
for i in range(size):
    num = int(input("Enter the number: "))
    nums +=[num]
i = 0
while i<size:
    total = 0
    num = nums[i]
    while num>0:
        total +=(num%10)
        num//=10
    if total >= 10:
        print(f"First Matching Number:{nums[i]}")
        break
    i+=1
else:
    print("There is no numbers given condition")

'''
Output:
Enter the size: 5
Enter the number: 123
Enter the number: 245
Enter the number: 341
Enter the number: 562
Enter the number: 901
First Matching Number:245
'''

