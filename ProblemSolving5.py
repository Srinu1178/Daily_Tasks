# Write a program to check whether a year is leap year or not
# first condition year%4==0 and year%100!=0
# second condition year%400 == 0

def leapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print(f'The year {year} is leap year')
    else:
        print(f'The year {year} is not a leap year')

leapYear(1996)
leapYear(2020)

'''
Output:
The year 1996 is leap year
The year 2020 is leap year
'''


# Write a program to return number of days in a month when we pass month and year as input

def NumOfDaysInMonth(month,year):
    if month == 2:
        if year%4==0 and year%100!=0 or year!=400:
            noOfdays = 29
        else:
            noOfdays = 28
    elif month==4 or month==6 or month==9 or month==11:
        noOfdays=30
    else:
        noOfdays = 31
    return f'The number of days in month {month} and year {year} are:{noOfdays}'

print(NumOfDaysInMonth(2,1996))

'''
Output:
The number of days in month 2 and year 1996 are:29
'''

# 3.Write a program to print all prime numbers btw a range.

def primeNumbers(start,stop):
    print(f"The prime numbers between {start} and {stop} are: ")
    countPrimes=0
    for num in range(start,stop+1):
        count = 0
        for j in range(1,num+1):
            if num%j==0:
                count+=1
        if count==2:
            print(num,end=' ')
            countPrimes+=1
    print(f'\n The number of primes in the given range:{countPrimes}')

primeNumbers(20,80)

'''
Output:
The prime numbers between 20 and 80 are:
23 29 31 37 41 43 47 53 59 61 67 71 73 79
The number of primes in the given range:14
'''


# 4. Write a program to check wheather a number is sunny number or not
#  A number n is called sunny number if n+1 is a perfect square
# Ex: 15 , 15+1 = 16 which is perfect square

def sunnyNum(num):
    temp = num+1
    if temp**0.5 == int(temp**0.5):
        print(f"{num} is sunny number")
    else:
        print(f'{num} is not sunny number')

sunnyNum(15)

'''
Output:
15 is sunny number
'''





