#nested for loop
for i in range(1,5):
    for j in range(1,5):
        print(i,j)


#WAP to print all the tables of numbers 1 to 10
print("Tables of 1 to 10")
for i in range(1,11):
    print(f'Table of {i}: ')
    for j in range(1,11):
        print(f'{i}X{j}={i*j}')


# Write a program to print common items between
# two lists

sarathFastFood = ['Chicken Fried Rice','Chicken Noodles','Manchuria','Chicken 65',
                  'Egg Rice','Chicken Majestic']

bhanuTejaRestaurant = ['Chicken Biryani','Soups','Chicken 65',
                       'Chicken Majestic']

for items in sarathFastFood:
    for items2 in bhanuTejaRestaurant:
        if items == items2:
            print(items)

i = 1
while i<=5:
    j=1
    while j<=5:
        print(i,j)
        j+=1
    i+=1

# write a nested while loop to calculat e total and average of 5 students
# in 5 subjects
student=1
while student<=5:
    subject=1
    total = 0
    while subject<=5:
        marks=int(input("Enter subject marks: "))
        total+=marks
        subject+=1
    print(f"Student {student} marks: {total}")
    average = total/5
    print(f'Total of Student is: {total} and average is:{average}')
    student+=1

# a restaurant has 3 customers and each one placed 4 items order,
# calculate total bill of each customer with 12% gst
customers = 1
while customers<=3:
    items = 1
    total = 0
    while items<=4:
        bill = int(input("Enter the each item bill: "))
        total+=bill
        items+=1
    total_bill = total*1.12
    print(f'Total Bill with gst_add: {total_bill}')
    customers+=1


# Track monthly expense of a person for 3 months for four categories in
# each month and print the highest expense in all three months.

month = 1
while month<=3:
    categories = 1
    max_amount = 0
    total = 0
    high_expense_category = 0
    while categories<=4:
        expenses = int(input(f'Enter the expenses {categories} and {month}: '))
        total+=expenses
        categories+=1
        if expenses > high_expense_category:
            high_expense_category=expenses
    print(f'Highest expensive per month category wise: {high_expense_category}')
    print(f'Total expense of month {month}:{total}')
    if total>max_amount:
        max_amount=total
    month+=1
print(f'Highest amount in 3 months: {max_amount}')


# Create a dashboard of runs scored by each player in a test cricket match
# and give man of the match to the person with highest score.

player_scores = []
max_score = 0
index = 0
for i in range(1,12):
    total = 0
    print(f'Player {index+1} is Playing: ')
    while True:
        score = int(input("Enter the runs per ball: "))
        total +=score
        if score == -1:
            break
    player_scores+=[total]
    if player_scores[index]>max_score:
        max_score=player_scores[index]
    index+=1
print(f"Man of the Match Score: {max_score}")

        










