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

  



