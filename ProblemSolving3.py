# Write a program to print sum and product of numbers from m to n

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
temp=m
sum_1 = 0
product = 1
while m<=n:
    sum_1+=m
    product*=m
    m+=1
print(f'sum of {temp} to {n}: {sum_1}')
print(f'product of {temp} to {n}: {product}')


m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
sum_1 = 0
product = 1
for num in range(m,n+1):
    sum_1+=m
    product*=m
print(sum_1)
print(product)



# write a program to print fibonnaci sequence numbers

num = int(input("Enter the fibonnaci number:"))
a = 0
b = 1
print(a,b,end=" ")
for i in range(1,num+1):
    c = a+b
    print(c,end=" ")
    a = b
    b = c

while loop
num = int(input("Enter how many fibonacci numbers you want: "))
a = 0
b = 1
i = 1
while i <= num:
    print(a,end=" ")
    c = a+b
    a = b
    b = c
    i+=1

# write a factorial number using while loop

num = int(input("Enter the factorial number: "))
fact =1
temp = num
while num>=1:
    fact *=num
    num-=1
print(f'factorial of given number {temp} is: {fact}') 

'''
Output:
Enter the factorial number: 5
factorial of given number 5 is: 120
'''

#  to check whaether the number is prime or not:
count = 0
num = int(input("Enter the number: "))
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count == 2:
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')


# check wheather the number is perfect square or not
num = int(input("Enter the number: "))
if num**0.5 == int(num**0.5):
    print(f'{num} is perfect square')
else:
    print(f'{num} is not perfect square')


# check wheather a number is perfect number or not

num = int(input("Enter the number: "))
sum_1 = 0
for i in range(1,num):
    if num%i==0:
        sum_1+=i
if sum_1 == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')


num = int(input("Enter the number: "))
sum_1 = 0
i = 1
while i<num:
    if num%i == 0:
        sum_1+=i
    i+=1
if sum_1 == num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')



