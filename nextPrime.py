n = int(input("Enter a number: "))
b = n+1
while True:
    p = True
    if b<2:
        p=False
    else:
        for i in range(2,b):
            if b%i==0:
                p=False
                break
    if p==True:
        print(b)
        break
    b+=1

