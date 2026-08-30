# write a program to count the number of factors of a number

n = int(input("Enter the number:"))
count = 0
i = 1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
print(f'Count the no of factors in the given number is {count}')   



m = int(input("starting number: "))
n = int(input("ending number: "))
evenList = []
oddList = []
even_count = 0
odd_count = 0
for num in range(m,n+1):
    if num%2==0:
        even_count+=1
        evenList+=[num]
    else:
        odd_count+=1
        oddList+=[num]
print(f'the even numbers btw {m} and {n}: {evenList}')
print(f'The even numbers btw {m} and {n} is : {even_count}')
print(f'the odd numbers btw {m} and {n}: {oddList}')
print(f'The odd numbers btw {m} and {n}: {odd_count}')


# write a program to print reverse of a string
s=input("Enter the string: ")
revStr = ''
i=0
while i<len(s): 
    revStr=s[i]+revStr
    i+=1
print(f'The reverse of the string {s} is {revStr}')

if s == revStr:
    print(f'The string {s} is palindrome')
else:
    print(f"The string {s} is not palindrome")


# Write a program to count numbers of vowels in a string 
str1 = input("Enter the string: ")
count = 0

for ele in str1:
    if ele in 'aeiou':
        count+=1
print(f'The number of vowels in the {str1}: {count}')

# Tasks
# 1. Write a program to print all vowels in a string with repetation
word = input("Enter the word: ")
vowels = 'aeiou'
vowels1 = ''
for ele in word:
    if ele in vowels:
        vowels1+=ele

print(f'vowels in the given word {word} is :{vowels1}')

'''
Output:
Enter the word: Python Programming
vowels in the given word Python Programming is :ooai
'''

# Write a program to print the count and consonants in a string

str2 = input("Enter the string: ")
vowels = 'aeiou'
count = 0
i = 0
while i<len(str2):
    if str2[i] not in vowels:
        count+=1
    i+=1
print(f'The Number of consonants in the {str2}:{count}')

'''
Output:
Enter the string: Hello World
The Number of consonants in the Hello World:8
'''

# write a program to print count and vowels in a string without repetation

str4 = input('Enter the string: ')
vowels = 'aeiou'
vowels1 = ''
i = 0
count = 0
while i < len(str4):
    if str4[i] in vowels:
        if str4[i] not in vowels1:
            count+=1
            vowels1+=str4[i]
    i+=1
print(f'The count of vowels without repetation: {count}')
print(f'The number of vowels in the string:{vowels1}')

'''
Output:
Enter the string: Srinivasu
The count of vowels without repetation: 3
The number of vowels in the string:iau
'''

# write a program to print count of alphabets,numbers and special characters
alphabets = 0
numbers = 0
special = 0
word5 = input("Enter the string: ")
i = 0
while i<len(word5):
    if ('A'<=word5[i]<='Z') or ('a'<=word5[i]<='z'):
        alphabets+=1
    elif ('0'<=word5[i]<='9'):
        numbers+=1
    elif word5[i]==' ':
        continue
    else:
        special+=1
    i+=1
print(f"No of alphabets in the {word5}:{alphabets}")
print(f"No of numbers in the {word5}:{numbers}")
print(f"No of special in the {word5}:{special}")

'''
Output:
Enter the string: Python@#3245
No of alphabets in the Python@#3245:6
No of numbers in the Python@#3245:4
No of special in the Python@#3245:2
'''




 

