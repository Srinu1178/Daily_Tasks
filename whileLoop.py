#Using while loop print all numbers from 1 to 10
i = 1 #initialization
while i<=10:
    print(i)
    i+=1
print("While loop ended")

# Even numbers
i=2
while i<=25:
    print(i)
    i+=2

# odd numbers
i=1
while i<=25:
    if i%2==1:
        print(i)
    i+=1

#WAP to print sum of all numbers from 1 to 100
sumOfNums = 0
i = 1 
while i<=100:
    sumOfNums+=i
    i+=1
print(f'The sum of numbbers is {sumOfNums}')


#str1 = "Python"
str1 = "Python"
i = 0
while i<len(str1):
    print(str1[i])
    i+=1

#WAP to print table of a number using while loop
num = int(input("Enter the number: "))
i = 1
while i<=10:
    print(f'{num}x{i}={num*i}')
    i+=1

# print all the numbers divisible by 3 from 1 to 30
i = 1
while i<=30:
    if i%3==0:
        print(i)
    i+=1

str2 = "Python sir teaching is good"

last_index = len(str2)-1
while last_index>=1:
    print(str2[last_index])
    last_index-=1


# WAP to keep guessing the secret number until the user enters
# correct
secretNum = 56
guess = 0
while guess!=secretNum:
    guess = int(input("Enter the guess number: "))
print("Your guess is correct")

#WAP to generate a new prices from a list of prices
# by adding 12% gst to each individual price
prices = [1299,1599,2599.3699,7999]
new_prices = []
for price in prices:
    new_prices+=[price*1.12]
print(new_prices)
