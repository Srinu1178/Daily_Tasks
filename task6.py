# Task: 
# 1. Write a function to check wheather a given date is valid or not, you pass three
#    parameters, for date,month, and year.

def validDate(date,month,year):
    if date>31 and month>12:
       print(f"Invalid date is {date}/{month}/{year}")
    elif year%4==0 and year%100!=0 or year%400 == 0:
        if month==4 or month==6 or month==9 or month==11:
                if date>30:
                    print(f"Invalid date is {date}/{month}/{year}")
                else:
                    print(f'The date {date}/{month}/{year} is valid')
        elif month==2:
            if date<=29:
                print(f'The date {date}/{month}/{year} is valid')
            else:
                print(f"Invalid date is {date}/{month}/{year}")
        else:
            print(f'The date {date}/{month}/{year} is valid')
    elif month==4 or month==6 or month==9 or month==11:
        if date>30:
           print(f"Invalid date is {date}/{month}/{year}")
        else:
            print(f'The date {date}/{month}/{year} is valid but not leap year')
    elif month==2:
        if date<=28:
            print(f"The date {date}/{month}/{year} is valid but not leap year")
        else:
            print(f"Invalid date is {date}/{month}/{year}")
    else:
        print(f"The date {date}/{month}/{year} is valid but not leap year")
validDate(3,7,2020)
validDate(4,2,1999)
validDate(31,2,2020)
'''
Output:
The date 3/7/2020 is valid
The date 4/2/1999 is valid but not leap year
Invalid date is 31/2/2020
'''

# 2. Write a function to print first prime number in a range
def firstPrime(start,stop): 
    for num in range(start,stop+1):
        count = 0
        firstPrime=False
        for j in range(1,num+1):
            if num%j==0:
                count+=1
        if count==2:
            print(f'The first prime number in the range {start} to {stop} is: {num}')
            break

firstPrime(10,20)
firstPrime(36,50)

'''
Output:
The first prime number in the range 10 to 20 is: 11
The first prime number in the range 36 to 50 is: 37
'''


# 3. Write a function to return last prime number
def lastPrime(start,stop):
    last_prime = 0
    for num in range(start,stop+1):
            count = 0
            for j in range(1,num+1):
                if num%j==0:
                    count+=1
            if count==2:
                last_prime=num
            if num==stop:
                return f'The last prime number in the range {start} to {stop} is: {last_prime}'

print(lastPrime(20,30))

'''
Output:
The last prime number in the range 20 to 30 is: 29
'''
    
# 4. write a function to print closest prime number to a number
def closestPrime(start,stop):
    flag=True
    first_prime = 0
    last_prime = 0
    for num in range(start,stop+1):
        count = 0
        for j in range(1,num+1):
            if num%j==0:
                count+=1
        if flag:
            if count==2:
                first_prime=num
                flag=False
        else:
            if count==2:
                last_prime=num
    count_first=0
    count_last = 0
    temp1 = first_prime
    temp2 = last_prime
    while temp1>start:
        count_first+=1
        temp1-=1
    while temp2<stop:
        count_last+=1
        temp2+=1
    if count_first<=count_last:
        return f'The closest prime number between range {start} and {stop} is: {first_prime}'
    else:
        return f'The closest prime number between range {start} and {stop} is: {last_prime}'

print(closestPrime(10,30))

'''
Output:
The closest prime number between range 10 and 30 is: 11
'''


# 5. Write a function to calculate sum of all prime numbers in a range
# and check whether the sum is prime or not.

def sumOfprimesCheck(start,stop):
    sum_primes = 0
    for num in range(start,stop+1):
        count=0
        for j in range(1,num+1):
            if num%j == 0:
                count+=1
        if count==2:
            sum_primes+=num
    count = 0
    for num in range(1,sum_primes+1):
        if sum_primes%num==0:
            count+=1
    if count == 2:
        return f'The sum of primes in the range {start} to {stop} is {sum_primes}. It is prime number'
    else:
        return f'The sum of primes in the range {start} to {stop} is {sum_primes}. It is not prime number'


print(sumOfprimesCheck(99,101))
print(sumOfprimesCheck(29,49))
'''
Ouput:
The sum of primes in the range 99 to 101 is 101. It is prime number
The sum of primes in the range 29 to 49 is 228. It is not prime number
'''







