
#lambda function

print((lambda num1,num2:num1+num2)(4,4))

print((lambda num1,num2:num1*num2)(5,50))



# write a lambda function to raise a number to a power

print((lambda a,b:a**b)(5,3))


# write a lambda function to find greatest among two numbers

print((lambda n1,n2: n1 if n1>n2 else n2)(10,20))


# write a lambad function to fine even or odd

res = lambda num: f'{num} is even' if num%2==0 else f'{num} is odd'

print(res(44))

# write a lambda function to perform sum of nums using variable length arguments

print((lambda *nums:sum(nums))(3,4,5,6))


#write a lambda function to convert a temp from cel to faen

print((lambda cel: (cel*9/5)+32)(32))





