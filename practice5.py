# STRINGS
#  1. Customer Name Initial Definition: A string is a sequence of characters.
#  Every character has a position called an index. 
# Real-Time Scenario & Task: A company wants to display the first letter of a 
# customer's name. Example Input: 'Rahul' Example Output: R 

name = input("Enter your name: ")
print(name[0])

'''
Ouptut:
Enter your name: Rahul
R
'''


# 2. Reverse Employee ID Definition: Strings can be reversed by accessing their
#  characters from the end toward the beginning. 
# Real-Time Scenario & Task: An office system needs to display an employee ID 
# in reverse order. Example Input: 'EMP1025' Example Output: 5201PME 

employeeId = input("Enter the employeeId: ")
i = 0
reverse=''
while i<len(employeeId):
    reverse=employeeId[i]+reverse
    i+=1
print(reverse)

'''
Output:
Enter the employeeId: EMP1025
5201PME
'''

# 3. Password Length Checker Definition: The length of a string is the number of 
# characters it contains.
#  Real-Time Scenario & Task: A website requires a password to contain at least 8 
# characters. Print 'Valid Password' when the requirement is satisfied;
#  otherwise print 'Invalid Password'. Example Input: 'Python123' 
# Example Output: Valid Password 
# Restriction / Hint: Try solving this using the 
# string length.

password = input("Enter the password: ")
if len(password)>=8:
    print("Valid Password")
else:
    print("Invalid Password")

'''
Output:
Enter the password: Python123
Valid Password
'''

# 4. Extract OTP from Message Definition: String indexing and slicing can be used to
# extract a specific part of a string. Real-Time Scenario & 
# Task: A mobile banking app receives an SMS containing a 6-digit OTP.
# Extract the OTP from the message. Example Input: 'Your OTP is 583921. 
# Do not share it.' 
# Example Output: 583921 Restriction / Hint: 
# Hint: Find where the OTP starts and use slicing.

msg = input("Enter the message: ")
pos = 0
for i in range(len(msg)):
    if '0'<=msg[i]<='9':
        pos=i
        break
otp=msg[pos:pos+6]
print(otp)

'''
Output:
Enter the message: Your OTP is 583921
583921
'''


#  5. Count Vowels in a Message Definition: A string can be processed character
#  by character using a loop.
#  Real-Time Scenario & Task: A messaging application wants to count the vowels 
# a, e, i, o and u in a message. Example Input: 'Python programming' 
# Example Output: 4 
# Restriction / Hint: Count vowels without using Counter.

msg = input("Enter the message: ")
vowels = 'aeiou'
i = 0
count = 0
while i < len(msg):
    if msg[i] in vowels:
        count+=1
    i+=1
print(count)

'''
Output:
Enter the message: Python Programming
4
'''


# LISTS 
# 6. Shopping Cart Total Definition: A list is an ordered collection that can contain
#  multiple values. Its elements can be processed using a loop. 
# Real-Time Scenario & Task: An online shopping cart contains the prices of 
# purchased products. Calculate the total price. 
# Example Input: [250, 120, 450, 300, 180] 
# Example Output: 1300 

cartPrices = [250,120,450,300,180]
total = 0
for price in cartPrices:
    total+=price
print(total)

'''
Output:
1300
'''


# 7. Find Highest Temperature Definition: List elements can be compared one 
# by one to find the largest value. 
# Real-Time Scenario & Task: A weather application stores temperatures
#  recorded over five days. Find the highest temperature.
#  Example Input: [32, 35, 31, 38, 34] Example Output: 38
#  Restriction / Hint: Restriction: Do not use max(). 

temperatures = [32,35,31,38,34]
i = 0
highTemp = 0
while i<len(temperatures):
    if temperatures[i]>highTemp:
        highTemp = temperatures[i]
    i+=1

print(highTemp)

'''
Output:
38
'''

# 8. Delivery Time Filter Definition: List filtering means selecting only the 
# elements that satisfy a condition. Real-Time Scenario & Task: 
# A delivery company records delivery times in minutes. 
# Print only deliveries that took more than 60 minutes. 
# Example Input: [45, 72, 35, 90, 55, 80] 
# Example Output: [72, 90, 80]

deliveryTime = [45,72,35,90,55,80]
highTime = []
i = 0
while i<len(deliveryTime):
    if deliveryTime[i]>60:
        highTime+=[deliveryTime[i]]
    i+=1
print(highTime)

'''
Output:
[72, 90, 80]
'''

# 9. Remove Failed Test Scores Definition: A list can be traversed and a new list can be
# created by keeping only the required values. 
# Real-Time Scenario & Task: A teacher stores students' test scores.
# A score of -1 means the student did not attend. Remove all -1 values. 
# Example Input: [85, -1, 72, 90, -1, 65]
# Example Output: [85, 72, 90, 65] 

score = [85,-1,72,90,-1,65]
i = 0
new_score = []
while i<len(score):
    if score[i]!=-1:
        new_score+=[score[i]]
    i+=1
print(new_score)

'''
Output:
[85, 72, 90, 65]
'''
    


# 10. Find a Product in Cart Definition: The membership operator can check whether a 
# particular value exists in a list. 
# Real-Time Scenario & Task: An online shopping cart contains product names. 
# Check whether the requested product is present. Print 'Product Found' or 
# 'Product Not Found'. 
# Example Input: Cart: ['laptop', 'mouse', 'keyboard', 'headphones'] 
# Search: 'mouse' Example Output: Product Found

cart = ['laptop','mouse','keyboard','headphones']
search = input("Search: ")
for product in cart:
    if search==product:
        print("Product Found")
        break
else:
    print("Product Not Found")

'''
Output:
Search: mouse
Product Found
'''

# DICTIONARIES 
# 11. Student Marks Total Definition: A dictionary stores information as key-value pairs. 
# A key can identify a subject and its value can store the marks. 
# Real-Time Scenario & Task: A school stores a student's marks in different subjects. 
# Calculate the total marks. Example Input: {'Python': 85, 'SQL': 72, 'Linux': 90}
# Example Output: 247 
marks = {'Python':85,'SQL':72,'Linux':90}
total = 0
for value in marks.values():
    total+=value

print(total)

'''
Output:
247
'''

#  12. Product Price Lookup Definition: A dictionary can associate a key, such as a
#  product name, with a value, such as its price. Real-Time Scenario & Task:
#  A store maintains product prices. Ask the user for a product name and display
#  its price. Example Input: Products: {'laptop': 55000, 'mouse': 800, 'keyboard': 1500}
#  Search: 'mouse' Example Output: Price: 800 

products = {'laptop': 55000, 'mouse': 800, 'keyboard': 1500}
search = input("Search: ")
for key in products.keys():
    if key==search:
        print(f'Price: {products[key]}')
        break
else:
    print("Product not found")

'''
Output:
Search: mouse
Price: 800
'''

# 13. Update Product Stock Definition: Dictionary values can be changed by assigning a
#  new value to an existing key. Real-Time Scenario & Task: A warehouse maintains
#  product stock. A shipment arrives containing 5 laptops. Update the laptop stock. 
# Example Input: {'laptop': 10, 'mouse': 25, 'keyboard': 15} 
# Example Output: {'laptop': 15, 'mouse': 25, 'keyboard': 15}

products = {'laptop': 10, 'mouse': 25, 'keyboard': 15} 
products['laptop']+=5
print(products)

'''
Output:
{'laptop': 15, 'mouse': 25, 'keyboard': 15}
'''

# 14. Find Highest Scorer Definition: Dictionary keys and values can be traversed 
# together to compare values and identify the corresponding key. 
# Real-Time Scenario & Task: A gaming application stores players and their scores.
#  Find the player with the highest score. 
# Example Input: {'Rahul': 85, 'Anil': 92, 'Kiran': 78, 'Vijay': 95}
#  Example Output: Vijay 95 Restriction / Hint: Restriction: Do not use max(). 

scores = {'Rahul': 85, 'Anil': 92, 'Kiran': 78, 'Vijay': 95}
name = ''
high_score = 0
for key,item in scores.items():
    if item>high_score:
        high_score=item
        name = key
print(f'{name} {high_score}')


# 15. Count Product Sales Definition: A dictionary can maintain a frequency count.
#  Each key represents an item and its value represents how many times it occurred.
#  Real-Time Scenario & Task: A shop records every product sold during the day.
#  Create a dictionary showing how many times each product was sold. 
# Example Input: ['laptop', 'mouse', 'laptop', 'keyboard', 'mouse', 'laptop'] 
# Example Output: {'laptop': 3, 'mouse': 2, 'keyboard': 1}
#  Restriction / Hint: Restriction: Do not use Counter.

records = ['laptop', 'mouse', 'laptop', 'keyboard', 'mouse', 'laptop'] 
new_records = {}
for ele in records:
    if ele in new_records:
        new_records[ele]+=1
    else:
        new_records[ele]=1
print(new_records)

'''
Output:
{'laptop': 3, 'mouse': 2, 'keyboard': 1}
'''
