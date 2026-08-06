for i in range(10):
    print('Hello')

# write a program with for loop and range to print numbers from n to 1

n = int(input("Enter the number: "))
for i in range(n,0,-1):
    print(i)

# wap to print each individual character in a string

str1 = 'data science'
for i in str1:
    print(i)

names = ['venkat','sarath','shankar','rasagna']
for name in names:
    print(name)

# wap to print all even numbers from 1 to 25
for num in range(1,26):
    if num%2 == 0:
        print(num)


# WAP to print all odd numbers in a list 1 to n
odd_num = []        
for num in range(1,26):
    if num%2 == 1:
        odd_num +=[num]
print(odd_num)

# wap a program to calculate total marks of a student
marks = [52,47,55,42,36,72]
total = 0
for mark in marks:
    total+=mark

print(f'Total is: {total}')

# WAP to count number of items in a bad

bag = ['chager','tshirt','short','tooth brush','tooth paste','power bank'
       ,'earpods']
count = 0
for item in bag:
    count+=1
print(f'No of items in the bag :{ count}')

# wap to add 12% gst to every price of an item and generate new prices

prices = [84999,123999,5999,29999,2999]
new_prices = []
for price in prices:
    new_prices +=[int(price*1.12)]
print(new_prices)

# Write a program to print length of each word in a list

words = ['venkat','narayana','artificial intelligence','10k coders',
         'Trainer','python']
for word in words:
    print(f'length of the {word} is : {len(word)}')

# Write a program to calculate total number of items in the stock

wholeSale = {'Rice Bags': 34,'Wheat Bags':21,'Maida Bags':3,
             'Oil Boxes': 11,'Shampoo Boxes':5}
total = 0
for stock in wholeSale.values():
    total+=stock

print(f'The total number of item stock is:{total}')


# Task: take marks of 5 subjects and find average and percentage using
# for loop

marks = [70,60,50,55,48]
sum_m = 0
percentage = 0
count = 0
for mark in marks:
    count+=1
    sum_m +=mark
print(f'average of marks in subject: {sum_m/count}')
print(f'percentage of marks in subjects: {(sum_m/(count*100))*100}%')





