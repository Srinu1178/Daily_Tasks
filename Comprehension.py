nums = [1,2,3,4,5]
com = [x*x for x in nums]
print(com)


nums = [1,2,3,4,5,6,7,8,9,10]
evenNums = [num for num in nums if num%2==0]
print(evenNums)
oddNums = [num for num in nums if num%2==1]
print(oddNums)

zeroMatrix = [[0]*3 for i in range(3)]
print(zeroMatrix)

# Write a comprehension to generate a list of names in upper case

names = ['kiran','sumanth','shankar','mahesh']
upperNames = [ch.upper() for ch in names]
print(upperNames)

# write a comprehension to generate list of nums from a list which are greater
# than 50 and less than 75

nums = [56,76,23,11,-2,707,43,90,71,76]
conNums = [num for num in nums if num>50 and num<75]
print(conNums)


costPrices = [11299,13999,15899,34999,56989]
#generate a list of selling prices by adding 10% of each price to iteself using
# comprehension

sellingPrices = [float(f'{price*1.10:.2f}') for price in costPrices]

print(sellingPrices)


emails = ['venkatanarayana@spacex.com','sumanthteja@tesla.com',
          'shankar@openAI.com','rasagna@asml.com']

username = [name.split("@")[0] for name in emails]
domain = [name.split("@")[1] for name in emails]
print(username)
print(domain)











