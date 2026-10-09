#Square pattern

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end = ' ')
    print()

'''
Output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

print("Rectangle: ")

k = 4
l = 8
for i in range(1,k+1):
    for j in range(1,l+1):
        print('*',end=' ')
    print()
    
'''
Output:
* * * * * * * * 
* * * * * * * * 
* * * * * * * * 
* * * * * * * * 
'''


print('Right angle traingle: ')
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

'''
Output:
* 
* * 
* * * 
* * * * 
* * * * * 
'''

print("Reverse Traingle")

n = 5
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end=" ")
    print()

'''
Output:
* * * * * 
* * * * 
* * * 
* * 
* 
'''

print("Right angle traingle")
n = 5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end = " ")
    print()

'''
Output:
        *
      * *
    * * *
  * * * *
* * * * * 
'''
print("Reverse")
n = 5
for i in range(n,0,-1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end = " ")
    print()

print("Isolates traingle")
n = 5
for i in range(n,0,-1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end = " ")
    print()

'''
Output:
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''

print("Isolates traingle: ")
n = 5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end = " ")
    print()

'''
Output:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end = " ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end = " ")
    print()


'''
Output:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''

