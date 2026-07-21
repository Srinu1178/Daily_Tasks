#Mutable and immutable
#Objects
#Immutable: Integer,float,complex,tuple,frozenset,string
#Mutable: List,dictionary,sets
list1 = [1,2,3,4,5]
print(list1)
print(id(list1))
list1 += [6,7,8,9]
print(list1)
print(id(list1))

int1 = 5
print(int1)
print(id(int1))
int1+=5
print(int1)
print(id(int1))

print("Float Values.....")
float1 = 55.4
print(float1)
print(id(float1))
float1+=10
print(float1)
print(id(float1))

print("Complex Values....")
comp1 = 2+3j
print(comp1)
print(id(comp1))
comp1 += 3+10j
print(comp1)
print(id(comp1)) 

# since set and dictionary are unordered we cannot use += for the
# |=
set1 = {'sarath','kavitha','bhargavi','bhanu teja'}
print(set1)
print(id(set1))
set1 |= {'anantha lakshmi','radhika'}
print(set1)
print(id(set1))

#dictionary
print("dictionary")
dict1 = {"name":"srinu","age":24,"edu":"MSC"}
print(dict1)
print(id(dict1))
dict1 |= {"place":"attili","pincode":534134}
print(dict1)
print(id(dict1))