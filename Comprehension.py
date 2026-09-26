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


#Set Comprehension

str1 = 'education'
setComp = {ch for ch in str1}

print(setComp)

steVowels = {ch for ch in str1 if ch in 'aeiou'}
print(steVowels)

# write a set comprehension to generate a set of all unique words from a string

bio = '''My name is venkata narayana and i have cold and cough and not able to 
take class but still taking class because I want salary'''


uniWords = {word for word in bio.split()}

print(uniWords)

# Dictionary comprehension
nums = [4,7,9,2,-1,3]

dictExp = {num:num**3 for num in nums}

print(dictExp)

words = ['python','Artificial Intelligence','Machine Learning','Java','D22 Class']

#generate a dictionary where len of each word is mapping
#to its word
wordDic = {len(word):word for word in words if len(word)>5}

print(wordDic)


temps = (34,56,23,55,12,-4)
# write a comprehension to generate a dictionary where each cel temp
#is mapping to its equivalent fahrenheit

dictCel = {temp:(temp*9/5)+32 for temp in temps}
print(dictCel)


marks = {'ipsitha':72,'benjaminu':32,'lankesh':66,
         'doritha':99,'eeston':21,'jadal':12.5,'peddi':100}

result = {key:"pass" if mark>35 else "Fail"  for key,mark in marks.items()}

print(result)


str1 = 'Sylvester Stallone'
# write a comprehension to generate a dict where each char is mapping to its number
# of occurences in the string

charMap = {ch:str1.count(ch) for ch in str1 if ch!=" "}
print(charMap)





