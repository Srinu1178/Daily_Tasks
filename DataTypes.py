#Data Type : It tells us what kind of data a value is.
#Note: In python we don't have primitive and non-primitive

#why
#Because in python everyvalue is an object so there are no primiitive and
# non premitive 
# Here we differntiate objects on the similarity in the data

# Numerical Data Type:
# It stores the values in the form of numbers
# eg: integers,float,complex
#integer: It is a whole number without decimal points. It can be +ve,-ve or 0

int1 = 10
print(type(int1))

#type() is used to check the data type of an object

#float(): It is a number with decimal point. It can also be positive,negative
# or zero
percentage = 99.99
cgpa = 8.89
temp = -12.5
print(type(percentage))
print(type(cgpa))
print(type(temp))

# complex: 
# It is a combination of real numbers and imaginary numbers

com1 = 2+5j
com2 = 3+4j

print(type(com1))

#real number: The part of complex number with no alphabet
#imaginary number: The part of complex number with alphabet j

# String Data Type
# It is a sequence of characters given between the quotes
name = "venkat"
username = "venkat46"
password = "Narayana@46"
print(type(name))

#Boolean Data Type:
# This data type store truth values
# truth value: Value you get when you execute the condition
# True and False are the two values only we have
a = 10>5
print(a)
print(type(a))

#Sequence data Type
# These are used to store multiple objects as one single object
# list and tuple
sem1marks = [62,83,59,45,70]
print(type(sem1marks))

#list: It stores multiple objects between square braces[]
# It can store objects of different data types as elements


#tuple: It is also used to store multiple objects as element

#-> but it is not editable
#-> It is given between () or round braces

tuple1 = (1,2,3,4,5)
print(type(tuple1))

#Dictionaries:
# It is the collection of key value pairs
# It is a mutable data type so we can add,delete and update the data
# we can execute the dictionary in the form of {'Key':'Values}

# -> Why the order is not changing in dictionary even though it is unordered

# Dictionary stores the values in it is order of the keys inserted into dictionary

details = {"name":"Bhai","age": 23, "place":"tirupati"}
print(details)

# set:
# Set stores unique values
# -> why the order in set does not change for numbers
# -> but changes for characters/strings
# -> because set stores values/objects based on their hash values
# and for numbers the hash values are themselves but for strings the hash
# values change every time execute your program
set1 = {1,2,3,4,5,6,889}
print(hash(1))
# note: hash() is the function we use to know the value of an object

# frozenset: It is a set which cannot be changed after creation
# note: when do we use tuple (or) frozenset
# We use them when we want to store values which should not be changed
# Example: Fuounder of company
# National bird and animal
#set stores unique values
# set stores only immutable/non changable elements
list3 = [12,34,5,6,7,8]
froz = frozenset(list3)
print(type(froz))

#None Data Type:
# ->It is used to represent absence of a value

def addition():
    a = 10
    b = 4
    a+b
print(addition())
