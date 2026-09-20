# Strong Number — 145 → 1!+4!+5! = 145

num = int(input("Enter the number: "))
sum1 = 0
temp = num
while temp>0:
    rem = temp%10
    fact = 1
    for num1 in range(1,rem+1):
        fact*=num1
    sum1+=fact
    temp//=10
if num == sum1:
    print(f"{num} is a strong number")
else:
    print(f'{num} is not a strong number')



'''
Output:
Enter the number: 145
145 is a strong number
'''