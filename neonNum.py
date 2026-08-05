n = int(input("Enter the number: "))
y = n*n
r = 0
while y>0:
    d = y%10
    r+=d
    y//=10
print(r)