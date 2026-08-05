num = int(input('Enter a number: '))
size = len(str(num))
temp = num
arm = 0
while temp>0:
    rem = num%10
    arm +=(rem**size)
    temp = temp//10
print(arm)