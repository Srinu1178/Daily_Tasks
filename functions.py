# # write a function to check the number is even or odd
# def evenOdd():
#     num = int(input("Enter the number: "))
#     if num%2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f'{num} is odd')

# # call the function
# evenOdd()

# # write a function to print all odd numbers from 1 to 50

# def oddNumbers():
#     for i in range(1,51):
#         if i%2==1:
#             print(i,end=' ')

# oddNumbers()

# # write a function to check the number wheather prime or not

# def isPrime():
#     num = int(input("Enter the number: "))
#     flag = True
#     if num<2:
#         print(f"{num} is not prime")
#     else:
#         for i in range(2,int(num**0.5)+1):
#             if num%2==0:
#                 flag=False
#                 break
#         if flag:
#             print(f'{num} is prime')
#         else:
#             print(f'{num} is not prime')
# isPrime()

# # write a function to print factorial of a number

# def factorial():
#     num = int(input("Enter the number: "))
#     fact = 1
#     for i in range(1,num+1):
#         fact = fact*i
#     print(f'the factorial of given number {num} is : {fact}')

# factorial()


# # Write a function to give discount to customer such that 
# # if customer makes a bill greater than 10000 give 10% discount
# # if bill>5000 give 5% discount
# # else give 2% discount

# def discountApply():
#     bill = int(input("Enter the bill: "))
#     if bill > 10000:
#         print(f'you got 10% discount : {bill*0.1} Total bill you pay: {bill-bill*0.1}')
#     elif bill>5000:
#         print(f'You got 5% discount :{bill*0.05} Total bill you pay: {bill-bill*0.05}')
#     else:
#         print(f'You got 2% discount: {bill*0.02} Total bill you pay: {bill-bill*0.02}')

# discountApply()