#WAP to calculate area of a retangle
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
area = length * breadth
print(f'Area of the rectangle is: {area:.2f}')

# WAP area of traingle
base = int(input("Enter the base of the traingle: "))
height = int(input("Enter the height of the traingle: "))
area = (1/2)*base*height
print(f'Area of the triangle is : {area}')

# perimeter of a square
side = int(input('Enter the side of the square:'))
peri = 4 * side
print(f'Perimeter of the square is: {peri}')

# perimeter of the rectangle
# peri = 2*(length+breadth)
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
peri = 2*(length+breadth)
print(f'perimeter of rectangle:{peri}')

# perimeter of the triangle
# peri = side1+side2+side3

side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

peri = side1+side2+side3
print(f'perimeter of the traingle is:{peri}')

# check whearther the given three sides forms a 
# traingle or not
# sum of any two sides must be greater than third side
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if (side1+side2)>side3 and (side2+side3)>side1 and (side3+side1)>side2:
    print("It is a form a traingle")
else:
    print("It is not form  a traingle")

#wap to calculate total marks of a student
marks = [62,83,76,100,75,72]
total = 0
for mark in marks:
    total+=mark
print(f'the total marks are : {total}')


#wap to calculate avg marks of a student
marks = [62,83,76,100,75,72]
total = 0
count = 0
for mark in marks:
    count +=1
    total+=mark
print(f'the avg of total marks are : {total/count}')

# Count How many 2000's,500's,100's and remaining amount
# in the given amount

amount = int(input("Enter the number: "))
notes_2000 = amount//2000
notes_500 = (amount%2000)//500
notes_100 = (amount%500)//100
remaining_notes = amount%100

print(f'2000 notes :{notes_2000}')
print(f'500 notes : {notes_500}')
print(f'100 notes: {notes_100}')
print(f'remaining notes:{remaining_notes}')


# convert given seconds into hours,minutes and remaining
# seconds
seconds = int(input("Enter the number of seconds"))
hours = seconds//3600
minutes = (seconds%3600)//60
remaining = (seconds%60)

print(f'Hours: {hours} hours')
print(f'Minutes: {minutes} mins')
print(f'remaining: {remaining} secs')