#Variable: It is a name that is referring pointing to a value/object
name = "Srinivasu"
print(name)
print(id(name)) #We have a function id() to know the address of an object

#id: The unique number assigned to the object when it is stored in heap.

# Assigning: The process of pointing an object with a variable is called assigning

#Types of assigning:
#1.Assigning: Pointing an object with a variable
#2. Reassigning: Two variables pointing to one object/value
#ii) one variable pointing to an object first later pointing to different object

venkat = "Trainer"
manoj = venkat

print(venkat)
print(manoj)

#Multiple assigning: Multiple variables pointing to one single object
# in one single line.

mat=fat=sis=mys="chicken"
print(mat)
print(fat)