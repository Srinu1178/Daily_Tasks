n = int(input("Enter the number: "))
for i in range(n):
    for j in range(n):
        print(chr(65+i+j*n),end=" ")
    print()