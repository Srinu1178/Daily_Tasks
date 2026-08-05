n = int(input("Enter a Number: "))
if n<2:
    print("Not a prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Not a prime")
            break
    else:
        print("prime")

