# Tuple Packing and Unpacking
#packing
num1,num2,num3 = 10,20,30
num1 = 10,20,30
print(num1)

#packing: When we pass multiple objects to a variable, it by default packs them
# into a tuple

values = 'venkat','Trainer','Pawan Kalyan Fan','Boxing Fan'
print(values)

#Unpacking: Using Multiple variables to access elements from a sequence

# string concatenation and replication:
str1 = 'Venkata'
str2 = 'Srinivasu'
print(str1+str2)

#string concatenation:
# Joining two strings togeather using + operator

# string replication:
# --> We can repeat a string multiple times using * operator

print("="*10)

#Decesion Making statements:
# --> Here the if statement takes a conditon and make one decesion if condition
# is true else makes another decesion
# syntax: rules to write a program
# if(condition):
   #code
# else:
#  code

# Is the person eligible to vote or not
age = int(input("Enter your age: "))
if age>=18:
    print("eligible")
else:
    print("not eligible")