# def printNumbers(num):
#     for i in range(1,num+1):
#         print(i)
#     print('Time Up')

# printNumbers(10) #normal function



# import time
# def printNums(num):
#     if num>10:
#         print("Time up")
#         return 
#     print(num)
#     time.sleep(1)
#     printNums(num+1)

# printNums(1)

# def printNumstoDec(num):
#     if num<1:
#         print("Time up")
#         return
#     print(num)
#     time.sleep(1)
#     printNumstoDec(num-1)
# printNumstoDec(10)



# def numAdds(num):
#     if num==5:
#         return num
#     return num+numAdds(num+1)

# print(numAdds(1))

# '''
# Output:
# 15
# '''

# def factorial(num):
#     if num==1:
#         return num
#     return num*factorial(num-1)

# print(factorial(5))

# '''
# Output:
# 120
# '''

# write a recursive function to count the number of digits in a number


# def countOfDigits(num):
#     if num == 0:
#         return num
#     return 1+countOfDigits(num//10)

# print(countOfDigits(240))

# '''
# Output:
# 3
# '''


# sum of digits


def SumOfDigits(num):
    if num==0:
        return num
    return num%10+SumOfDigits(num//10)

print(SumOfDigits(240)) 


def prodOfDigits(num):
    if num==0:
        return 1
    return num%10 * prodOfDigits(num//10)

print(prodOfDigits(244))

'''
Output:

'''

# Write a recursive function to find prod of digits


# write a recursive function to access each individual element in a nested structure


def nesStruc(seq,i=0):
    if i==len(seq):
        return 
    if isinstance(seq[i],list):
        nesStruc(seq[i])
    else:
        print(seq[i])
    nesStruc(seq,i+1)

nes= [1,[2,3],[4,[5,6]]]
nesStruc(nes)






