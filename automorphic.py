#automorphic number
n = int(input("Enter the number: "))
square = n*n
digits = 0
temp = n
while temp>0:
  digits+=1
  temp//=10
divisor = 10**digits
if square%divisor == n:
  print("Automorphic number")
else:
  print("Not Automorphic number")

'''
Output:
Enter the number: 76
Automorphic number
'''