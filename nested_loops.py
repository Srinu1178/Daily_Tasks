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