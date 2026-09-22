# Method: Method is also a function but it is attached to an object

# -> String methods:
# These are the functions which are attached to  string object

#Upper():
name = 'Bhai'
print(name.upper())



#lower():
com = "GOOGLE"
lowerCase = com.lower()
print(lowerCase)

#title:
movie = "avengers end game"
print(movie.title())

#split()
names = 'Venkat.bhai.srinu.koji.hasira'
print(names.split("."))
print(names.lower().upper().title().split("."))

#replace()

objective = "I like Java, Java is one of the most powerful programming Language"
changeObj = objective.replace("Java","Python")
print(changeObj)


#join():
# It does opposite of split

list1 = ["Python","ML","AI","Game Development"]

print(" ".join(list1))


bio = "I started data science but i dont know why i started data science"

print(bio.lower().upper().title().replace("Data Science","AI"))


# List Methods:
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)
list1.insert(1,1.5)
print(list1)

list1.insert(4,3.7)
print(list1)


#Extend(): To add multiple elements to an existing list at once
# We need to pass the elements as a list or tuple to add to the list
list1.extend([7,8,9,10,11,12])

print(list1)

#remove():

list1.remove(1.5)
list1.remove(3.7)
# list1.remove(20)
print(list1)

nums = [1,4,6,4,2,1,3,5]

nums.remove(4)
print(nums)


#sort:

list1 = [45,23,54,19,12,11,33]
list1.sort()
print(list1)

list_names =["rakesh",'srinu','manoj','ravi','bhai'] #based on asci values of each characcter for sorting
list_names.sort()
print(list_names)

# reverse()
list1 = [10,12,13]
list1.reverse()
print(list1)

#tuple methods
#count
nums = [4,5,6,3,4,5,6,3,5,6,3,56,1,2,4]
print(nums.count(4))

#index
print(nums.index(5))

#set methods

trainers={"venkat","navinder","manoj",'nayab'}

trainers.add("Subramanyam")
print(trainers)

trainers.update(['Bhai','Rechel'])
 
print(trainers)

set1 = {1,2,3}
set2 = {1,2,3,4}
print(set1.issubset(set2))
print(set2.issuperset(set1))

print(set1.union(set2)) 


#dictionary Methods
details = {'name':'balu','city':'SR Nagar'}
print(details['city'])

details['city'] = 'Bangalore'
print(details)
print(details["city"])

details['phone'] = 9805678124

print(details)

print(details.get('name'))

print(details.get('quali',"qualification does not exist"))







