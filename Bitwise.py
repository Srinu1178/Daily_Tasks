# Bitwise operators: It is used to perform operations on numbers at the level 
# of their bits

#  bitwise and (&):
#  It compares two binary values and returns 1 when both binary values are 1.

print(3&5)

#bitwise or (|):
# It compares two binary values and returns 1 when atleast one of them is 1.

print(5|7)
# bitwise left shift <<:
# number * 2**n
print(5<<2)

#bitwise right shift >>:
# number//2**n

print(5>>2)

#bitwise not or negation
# Note : Computer doesnot store negative numbers
print(~5)

# it flips every bit in a binary value from 0 to 1 and 1 to 0 including the symbol

# -6 = 2's complement 6
# formula = -(n+1)
print("task: ")
print(3<<3)
print(4<<6)

print(6>>2)
print(2>>2)

print(~9)
print(~8)
print(~-9)

#Warlus Operator:
# It is used to assign an object and pass it into an operation in the same line
print(name:="venkat")

# without warlus
length = len("srinu")
if length>8:
    print("Strong")
else:
    print("Not Strong")

# With Warlus
if (length:=len("srinivasu")):
    print("strong name")
else:
    print("Not strong")