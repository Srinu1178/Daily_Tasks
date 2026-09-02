# positional arguments
#write a function to welcome a student to our class
def welcome(name,course):
    return f'Welcome {name} to 10k coders, hope you do great in your {course} course'


# print(welcome('Bhai','Data Science'))
print(welcome('Data Science','Lazer'))

# write a function to find area of rectangle and circle using positional 
# arguments

def areaOfrectangleCircle(length,breadth,radius):
    areaRectangle = length * breadth
    areaCircle = 3.14*radius*radius
    return f'area of rectangle:{areaRectangle}\narea of circle:{areaCircle}'

print(areaOfrectangleCircle(10,8,7))

# write a function to print count of numbers from start to
#stop as parameters using while loop

def countNumbers(start,stop):
    temp = start
    count = 0
    while temp<=stop:
        count+=1
        temp+=1
    return f'The count of numbers between {start} and {stop} is :{count}'

print(countNumbers(10,25))

# default arguments:

def welcome(name="Guest"):
    return f'Welcome {name}, hope you have a great stay.'
print(welcome('Bhai'))
print(welcome())

# write a function to calculate total bill of restaurant with parameters
# for price and delivery charge, with 50 rs as default delivery charges

def calculateBill(price,del_charges=50):
    bill = price + del_charges
    return f'The total bill is: {bill}'

# print(calculateBill(500,60))
print(calculateBill(1000))


# write a function to calculate perimeter of a circle with parameters for
# radius and pi and pass default value for pi

def perimeterCircle(radius,pi=3.14):
    peri = 2*pi*radius
    return f'The perimeter of the circle with radius {radius} is: {peri}'

print(perimeterCircle(7))













