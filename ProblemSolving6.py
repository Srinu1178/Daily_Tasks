# Numbers: 
# 1. check whether a number is spy number or not
num = int(input("Enter the number:"))

def spyNum(num):
    temp = num
    sum1 = 0
    prd = 1
    while temp>0:
        rem = temp%10
        sum1+=rem
        prd *=rem
        temp//=10
    if sum1==prd:
        print(f'{num} is a spy number')
    else:
        print(f'{num} is not a spy number')

spyNum(num)

'''
Output:
Enter the number:123
123 is a spy number
'''

# print all spy numbers from given range 

def spyNumPrint(start,stop):
    print(f'The spy numbers between {start} and {stop} is:')
    for ele in range(start,stop):
        temp = ele
        sum1 = 0
        prod = 1
        while temp>0:
            last = temp%10
            sum1 += last
            prod *= last
            temp //=10
        if sum1 == prod:
            print(ele,end = ', ')

start = int(input("Enter the starting number: "))
stop = int(input("Enter the stoping number: "))
spyNumPrint(start,stop)


'''
Output:
Enter the starting number: 100
Enter the stoping number: 500
The spy numbers between 100 and 500 is:
123, 132, 213, 231, 312, 321,

Enter the starting number: 1
Enter the stoping number: 1000
The spy numbers between 1 and 1000 is:
1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 123, 132, 213, 231, 312, 321, 
'''


# Harshad Number

num = int(input("Enter the number: "))
def harshadNum(num):
    temp = num
    sum1 = 0
    while temp>0:
        last = temp%10
        sum1+=last
        temp//=10
    if num%sum1 == 0:
        print(f'{num} is a harshad number')
    else:
        print(f'{num} is not a harshad number')

harshadNum(num)

'''
Output:
Enter the number: 18
18 is a harshad number
'''

#


def harshadNum(start,stop):
    print(f'The harshad numbers between {start} and {stop}: ')
    while start<=stop:
        temp = start
        sum1 = 0
        while temp>0:
            last = temp%10
            sum1+=last
            temp//=10
        if start%sum1 == 0:
            print(start,end=',')
        start+=1

harshadNum(1,100)

'''
Output:
The harshad numbers between 1 and 100: 
1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42,45,48,50,54,60,63,70,72,80,81,84,90,100,

'''



# check whether the number is Arm Strong Number or not

def ArmStrongNumber(num):
    count = 0
    temp = num
    temp1 = num
    sum1 = 0
    while temp>0:
        count+=1
        temp//=10
    while temp1>0:
        last = temp1%10
        sum1+=last**count
        temp1//=10
    if num == sum1:
        print(f'{num} is an arm strong number')
    else:
        print(f'{num} is not an arm strong number')


num = int(input("Enter the number: "))
ArmStrongNumber(num)

'''
Output:
Enter the number: 153
153 is an arm strong number
'''


def ArmStrongNumber(num):
    i = 1
    num2 = 150
    while True:
        count = 0
        temp = num2
        temp1 = num2
        sum1 = 0
        while temp>0:
            count+=1
            temp//=10
        while temp1>0:
            last = temp1%10
            sum1+=last**count
            temp1//=10
        if num2 == sum1:
            print(num2,end=" ")
            i+=1
            num2+=1
        else:
            num2+=1
        if i == num:
            break


num = int(input("How many armstrong numbers you want: "))
ArmStrongNumber(num)



# 4. Automorphic number


def automorphicNum(num):
    temp = num
    square = num*num
    count = 0
    while temp>0:
        temp//=10
        count+=1
    divisor = 10**count
    if square%divisor==num:
        print(f'{num} is automorphic number')
    else:
        print(f'{num} is not automorphic number')

automorphicNum(76)

'''
Output:
76 is automorphic number
'''

# Task: Neon number: 
# sum of the digits of its square is equal to the original number.

def neonNumber(num):
    sum1 = 0
    square = num*num
    while square>0:
        digit = square%10
        sum1 +=digit
        square//=10
    if sum1==num:
        print(f'{num} is a neon number')
    else:
        print(f'{num} is not a neon number')

num = int(input("Enter the Number: "))
neonNumber(num)

'''
# Output:
# Enter the Number: 9
# 9 is a neon number
# '''    





















