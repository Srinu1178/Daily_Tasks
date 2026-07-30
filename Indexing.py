#Indexing and slicing
# --> Index numbers: For an ordered sequence each element in the sequence
# is assigned with a nunber based on its position, while we run the program
# --> since the index numbers of any ordered sequence are starting from 0 so we
# can pyrhon does zero based indexing
#  for n elements the possible index values are 0 to n-1

# Indexing: Accessing or editing elements in a sequence using index numbers is called
# indexing
# Example: Accessing elements in a string using index numbers
name = 'venkat'
print(name[2])

# Using indexing we have accessed and edited in a list
marks = [45,54,67,46,55,32]
print(marks[2])
marks[2] = 36
print(marks)

# Indexing done by using positive numbers is called positive indexing
# Indexing done by using negative numbers is called negative indexing

fruits = ['guava','apple','banana','mango','orange']
print(fruits[-4])
print(fruits[-1])

#Double Indexing: 
# It is using of nested indexing inside sequence sequences
kalakarulu = ['Jayadeep','durga sree','shankar','dinesh','bhargav']
print(kalakarulu[2][4])

#Task
bio = ['venkat narayana','Msc Computer science','Tech Trainer',
      ['python','machine learning','Artificial Intelligence','Robotics','Cyber security']]

#print M from MSC
print(bio[1][0])
#print a from Tech Trainer
print(bio[2][7])
#print c from Cyber Security
print(bio[3][4][0])

#slicing
# It is used to access (or) edit multiple elements from a sequence
# Finding top 3 students from list of topper
marks = [8.7,8.57,8.5,8.43,8.32]
print(marks[0:3])

backbenchers = [6.5,6.43,6.23,5.50,4.83]
backbenchers[2:5] = [9.0,9.5,9.99]

# Editing last 3 values of backbenchers
print(backbenchers)

#omitted values in slicing

tuple1 = (1,2,3,4,5,6,7,8,9,10)
print(tuple1[0:10])

# These are the values passed by default when no value is given in slicing
print(tuple1[:5])
print(tuple1[::])
print(tuple1[::3])

tech = 'Machine Learning'
print(tech[::-1])
# It negative step to jump on elements from list

