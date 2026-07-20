#Type conversion vs Type Casting
#Type Conversion: The automatic change of data type when we perform 
#operation between two different data types is called type conversion.

bool1 = True # By default the numerical value of True is 1
num = 12
total = bool1+num
print(total)

bool2 = False
fit1 = 22.3
print(bool2 + fit1)

# Type conversion is only possible between supportive data types.

com1 = 3+4j
num1 = 10.67
total = com1 + num1
print(total)


#Type Casting: 
print("Type Casting......")
salary = 25000 #integer
print(float(salary)) #i am converting integer value into float using
#float function

#Type casting: Here the user changes the data type of an object manually.
# - We Use data type functions to type cast one data object to other data object.


num1 = 22.5
print(int(num1)) #TypeCasting: 

#com1 = 2+3j
#print(int(com1)) # Note: It gives error 

num2 = 25
print(complex(num2))

num3 = 199
strNum = str(num3)
print(type(strNum))

list1 = [10,20,30,40]
print(tuple(list1))

# Dynamically Typed: Here we don't have to mention the type of the value
# we are passing them in to our program, we just pass the values and python 
# automatically assigns data type to them based on the values.


#range(): It is used to generate numbers.
list1 = [1,2,3,4,5,6,7,8,9,10]

print(list(range(1,11)))

# It takes three values start,stop and step
# Syntax: Rules to write a program
# range(start,stop,step)
# start: From which numbers to generate numbers
# stop: Until Which number to generate
# step: How many values to jump on

print(list(range(10)))

# when you pass only one value in the range
# it takes it as end value and by default
# it starts from 0

#negative step: used to generate numbers in reverse
print(list(range(25,0,-1)))

#len(): It returns the number of objects in a sequence
name = 'venkat'
print(len(name))
fullname = 'Venkata Srinivasu'
print(len(fullname))

list1 = [1,2,3,4,5,6,78,90]
print(len(list1))

dict1 = {"name":"srinu","qual":"MSC","prof":"Trainee"}
print(len(dict1))
