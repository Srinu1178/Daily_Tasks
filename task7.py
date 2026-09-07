# 1. Count Vowels Definition: A vowel is one of the letters a, e, i, o, or u. 
# Counting vowels means finding how many vowel characters are present in a 
# string. Task: Given a string, count the number of vowels in it. 
# Example Input: Input: 'education' 
# Example Output: Output: 5

def countVowels(word):
    count = 0
    for w in word:
        if w in 'aeiou':
            count+=1
    print(f'Output: {count}') 

word = input("Input: ")
countVowels(word)

'''
Output:
Input: education
Output: 5
'''

#  2. Count Words Definition: A word is a group of characters separated
#  by spaces. Counting words means finding the total number of words
#  in a sentence. Task: Given a sentence, count how many words it contains. 
# Example Input: Input: 'Python is easy' 
# Example Output: Output: 3

def countWords(sentence):
    count=0
    for word in sentence:
        if word==' ':
            count+=1
    print(f'Output: {count+1}')
sentence = input("Input: ")
countWords(sentence)

'''
Output:
Input: Python is easy
Output: 3
'''

#  3. Reverse a String Definition: Reversing a string means arranging its 
# characters from the last character to the first character.
#  Task: Given a string, create its reverse. Example
#  Input: Input: 'python' Example Output:
#  Output: 'nohtyp'

def reverseString(word):
    rev = ''
    for w in word:
        rev = w+rev
    print(f'Output: {rev}')

word = input("Input: ")
reverseString(word)

'''
Output:
Input: Python
Output: nohtyP
'''

# 4. Find the Largest Number in a List Definition: The largest number is the 
# element in a list whose value is greater than or equal to all other elements.
# Task: Find the largest number without using the max() function. 
# Example Input: Input: [12, 45, 7, 89, 23] 
# Example Output: Output: 89

def largestNumber(data):
    largest = data[0]
    for num in data:
        if num>largest:
            largest = num
    print(f'Output:{largest}')

data = [12,45,7,89,23]
largestNumber(data)
'''
Output:
Output:89
'''

# 5.Find the Smallest Number in a List Definition: The smallest number is the
# element in a list whose value is less than or equal to all other elements.
# Task: Find the smallest number without using the min() function. 
# Example Input: Input: [34, 12, 56, 8, 29] 
# Example Output: Output: 8 

def smallestNum(data):
    smallest = data[0]
    for num in data:
        if num<smallest:
            smallest=num
    print(f'Output:{smallest}')

data = [34, 12, 56, 8, 29]
smallestNum(data)

'''
Output:
Output:8
'''

# 6. Count Even and Odd Numbers Definition: An even number is divisible by 2 
# with no remainder. An odd number leaves a remainder of 1 when divided by 2. 
# Task: Given a list of numbers, count how many are even and how many are odd.
#  Example Input: Input: [10, 15, 22, 7, 8, 13]
#  Example Output: Output: 
# Even: 3,
#  Odd: 3 

def countEvenOdd(data):
    even = 0
    odd = 0
    for num in data:
        if num%2==0:
            even+=1
        else:
            odd+=1
    print(f'Output:\nEven: {even}, Odd:{odd} ')

data = [10, 15, 22, 7, 8, 13]
countEvenOdd(data)

'''
Output:
Output:
Even: 3, Odd:3 
'''


# 7. Check Palindrome String Definition: A palindrome is a string that remains
#  the same when read from left to right or right to left. 
# Task: Check whether a given string is a palindrome. 
# Example Input: Input: 'madam' Example 
# Output: Output:
#  Palindrome 

def isPalindrome(word):
    rev=''
    for w in word:
        rev=w+rev
    if word==rev:
        print(f'Palindrome')
    else:
        print(f'Not Palindrome')

word=input("Input: ")

isPalindrome(word)

'''
Output:
Input: madam
Palindrome
'''

# 8. Find a Number in a List Definition: Searching means checking whether a 
# particular value is present in a collection such as a list. 
# Task: Given a list and a number, check whether the number exists 
# in the list. Example Input: Input: [10, 20, 30, 40, 50],
#  Search: 30 
# Example Output: Output: Found
def searchNum(data,search):
    for num in data:
        if search == num:
            print(f'Found')
            break
    else:
        print("Not Found")


data=[10,20,30,40,50]
search = int(input("Search: "))
searchNum(data,search)

'''
Output:
Search: 30
Found
'''




# 9.Replace Spaces with Hyphens Definition: A space is a blank character 
# between words. Replacing spaces means changing each space character into
# another character. Task: Replace every space in a string with '-'.
# Example Input: Input: 'Python is fun'
# Example Output: Output: 'Python-is-fun' 

def replaceHyphens(word):
    new=''
    for w in word:
        if w==' ':
            new+='-'
        else:
            new+=w
    print(f'Output: {new}')

word= input("Input: ")
replaceHyphens(word)

'''
Output:
Input: Python is fun
Output: Python-is-fun
'''


# 10. Calculate the Sum of List Elements Definition: The sum of a list is the
# total obtained by adding all its numeric elements. Task: Find the sum of
# all numbers in a list without using the sum() function. 
# Example Input: Input: [10, 20, 30, 40]
# Example Output: Output: 100 

def sumOfelements(data):
    total = 0
    for ele in data:
        total+=ele
    print(f'Output: {total}')

data = [10,20,30,40]

sumOfelements(data)

'''
Output:
Output: 100
'''

# 11. Convert Lowercase to Uppercase Definition: Lowercase letters are small 
# letters such as a, b, and c. Uppercase letters are capital letters such as 
# A, B, and C. Task: Convert all lowercase letters in a string to uppercase.
#  Example Input: Input: 'python programming' 
# Example Output:
#  Output: 'PYTHON PROGRAMMING'

def conUpper(word):
    new = ''
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for w in word:
        found = False
        for i in range(26):
            if w==lower[i]:
                new+=upper[i]
                found = True
                break
        if not found:
            new+=w
    print(f'Output: {new}')

word = input("Input: ")
conUpper(word)

'''
Output:
Input: python programming
Output: PYTHON PROGRAMMING
'''

#  12. Print Elements Greater Than 10 Definition:
#  A number is greater than 10 when its value is more than 10. 
# Task: Given a list, print only the numbers greater than 10. 
# Example Input: Input: [5, 15, 8, 22, 3, 17] Example Output:
#  Output: 15 22 17 

def greaterThan10(data):
    print("Output:",end=" ")
    for num in data:
        if num>10:
            print(num,end=' ')

data=[5, 15, 8, 22, 3, 17]

greaterThan10(data)

'''
Output:
Output: 15 22 17 
'''

# 13. Count a Particular Character Definition: Character counting means 
# finding how many times a specified character occurs in a string. 
# Task: Given a string and a character, count how many times that character
#  appears. Example Input: Input: 'programming', Character: 'g' 
# Example Output: Output: 2

def charOccurs(word,char):
    count = 0
    for ch in word:
        if ch==char:
            count+=1
    print(f'Output: {count}')

word = input("Input: ")
char = input("Character: ")
charOccurs(word,char)

'''
Output:
Input: programming
Character: g
Output: 2
'''

# 14. Create a List of Squares Definition: The square of a number is the 
# number multiplied by itself. For example, the square of 4 is 16.
#  Task: Given a list of numbers, create a new list containing the square 
# of each number. Example Input: Input: [2, 4, 6, 8]
# Example Output: Output: [4, 16, 36, 64] 

def squaresList(data):
    new = []
    for num in data:
        new+=[num*num]
    print(f'Output:{new}')

data = [2, 4, 6, 8]
squaresList(data)

'''
Output:
Output:[4, 16, 36, 64]
'''

# 15.Find the Second Largest Number Definition: The second largest number is
# the number that comes immediately after the largest number when the 
# distinct values are arranged in descending order. Task: Given a list of
# different numbers, find the second largest number.
#  Example Input: Input: [10, 25, 7, 40, 18]
#  Example Output: Output: 25

def secondLargest(data):
    largest = data[0]
    secLargest = float('-inf')
    for num in data:
        if num>largest:
            largest=num
    for num in data:
        if num>secLargest and num<largest:
            secLargest=num
    print(f'Output:{secLargest}')

data = [10,25,7,40,18]

secondLargest(data)

'''
Output:
Output:25
'''
