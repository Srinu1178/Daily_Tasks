# #check wheather a number is even or odd
# num = int(input("Enter the number:"))
# if num%2 == 0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')

# #check wheather a number is divisible by 5 but not divisible
# # by 10

# num = int(input("Enter the Number: "))
# if num%5==0 and num%10!=0:
#     print(f'{num} is divisible only 5 not 10')
# else:
#     print(f'{num} doesnot satisfy the condition')


# # biggest among two numbers
# num1 = int(input("Enter the number: "))
# num2 = int(input("Enter the second number: "))
# if num1>num2:
#     print(f'{num1} is greater than {num2}')
# elif num2>num1:
#     print(f'{num2} is greater than {num1}')
# else:
#     print("Both are equal")

# #smallest among two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1<num2:
#     print(f'{num1} is less than {num2}')
# elif num2<num1:
#     print(f'{num2} is less than {num1}')
# else:
#     print('Both are equal')


#check wheather a number is divisible by 2,3 and 6

num3 = int(input("Enter the number: "))
if num3%2 == 0 and num3%3==0 and num3%6==0:
    print(f'{num3} is satisfy all the conditions')
else:
    print(f'{num3} is not satisfy the conditions')


# take three subjects marks as input and a student
# passes only when he gets >=36 in every subject

marks = {"Maths":35,"Physics":50,"Chemistry":60}
pas_exam = True
key = 0
for mark in marks.keys():
    if marks[mark]<=36:
        pas_exam = False
        break
if pas_exam:
    print("Pass")
else:
    print("Fail")

    


#write to check wheather a student passed or failed
# if he passes in any one of the subjects
prom = False
for mark in marks.keys():
    if marks[mark]>=36:
        prom = True
        break
if prom:
    print("Pass the exam")
else:
    print("Fail the exam")

# a student passes when he pass in atlesat any two of three
#subjects
pass_sub = 0
for sub,mark in marks.items():
    if mark>=35:
        pass_sub +=1
if pass_sub>=2:
    print("Pass the Exam")
else:
    print("Fail")


#Greatest among three numbers

num1 = 45
num2 = 45
num3 = 30
if num1>num2 and num1>num3:
    print(f'{num1} is greatest than {num2} and {num3}')
elif num2>num1 and num2>num3:
    print(f'{num2} is greatest than {num1} and {num3}')
elif num1==num2 and num2==num3:
    print("All numbers are equal")
elif num1 == num2:
    if num3>num1:
        print(f"{num3} is greater than {num1} and {num2}")
    else:
        print(f"{num1} and {num2} are greater than{num3}")
elif num2==num3:
    if num1>num3:
        print(f'{num1} is greater than {num2} and {num3}')
    else:
        print(f'{num2} and {num3} are greater than {num1}')
elif num1==num3:
    if num2>num3:
        print(f'{num2} is greater than {num1} and {num3}')
    else:
        print(f'{num1} and {num2} are greater than {num3}')

else:
    print(f'{num3} is greatest than {num1} and {num2}')


#task
#also handle all types of test cases
#WAP to find smallest among three numbers
#wap to find second largest among three numbers
#WAP to find second smallest among three numbers



