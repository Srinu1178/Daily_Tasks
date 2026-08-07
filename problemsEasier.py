# Problem 1: Student Initials Definition: Schools display initials. 
# Task: Input first and last name. Print first letter of each. 
# Example Input: First: Rahul Last: Sharma 
# Example Output: Initials: RS

first = input("Enter First Name:")
last = input("Enter last Name: ")

print(f'{first[0]}{last[0]}')

# Problem 2: Login Eligibility Definition: Classify account by age. 
# Task: <13 Child, 13-17 Teen, 18+ Adult.
#  Example Input: Age:16 Example Output: Teen Account

age = int(input("Enter the age: "))
if age < 13:
    print("Child Account")
elif age <= 17:
    print("Teen Account")
else:
    print("Adult Account")

# Problem 3: Check First and Last Character 
# Definition: Compare first and last characters. 
# Task: Print Same or Different. Example Input: level 
# Example Output: Same
word = input("Enter the word: ")
if word[0]==word[-1]:
    print("Same")
else:
    print("Different")

# Problem 4: Count Uppercase Letters
# Definition: Count uppercase letters. Task: Use one for loop. 
# Example Input: PyTHon Example Output: Uppercase Letters: 3

letter = input("Enter the letter: ")
count = 0
for word in letter:
    if word.isupper():
        count+=1
print(count)

# Problem 5: Shopping Discount Definition: Discount by bill. 
# Task: 5000+20%,3000+10%,else none. 
# Example Input: Bill:6000 Example Output: Discount:20% Payable Amount:4800

bill = int(input("Enter the bill: "))
if bill>=5000:
    print(f'Discount:20% Payable Amount:{bill-(bill*(20/100))}')
elif bill>=3000:
    print(f'Discount: 10% Payable Amount:{bill-(bill*(10/100))}')
else:
    print(None)

# Problem 6: Count Digits Definition: Count digits in string.
# Task: Use one for loop.Example Input: Python2026 
# Example Output: Digits: 4
digit_alpha = input("Enter the input: ")
count = 0
for digit in digit_alpha:
    if digit.isdigit():
        count+=1
print(count)

# Problem 7: Membership Validation Definition: 
# Validate membership. Task: Age>=18 then Gold/Silver. 
# Example Input: Age:22 Gold Example Output: Premium Access
age = int(input("Enter the age: "))
access = input("Gold or Silver: ")
if age>=18:
    if access == "Gold":
        print("Premium access")
    else:
        print("Normal Access")
else:
    print("Not access")

# Problem 8: Print Odd Index Characters
# Definition: Print odd index chars.
# Task: Use one for loop.
# Example Input: Programming 
# Example Output: rgamn

word = input("Enter the word: ")
for num in range(1,len(word)):
    if num%2==1:
        print(word[num],end="")
print()

# Problem 9: Password Length Checker 
# Definition:Check password strength by length. 
# Task: <8 Weak,8-11 Medium,12+ Strong. 
# Example Input: Python123 
# Example Output: Medium Password

password = input("Enter the password: ")
if len(password)<8:
    print("Weak Password")
elif len(password)<=11:
    print('Medium Password')
else:
    print("Strong Password")

# Problem 10: Vowel Counter Definition: Count vowels.
# Task: Use one for loop. 
# Example Input: Education 
# Example Output: Vowels: 5
word = input("Enter the word: ")
vowel_count = 0
for w in word:
    if w in 'aeiouAEIOU':
        vowel_count+=1
print(vowel_count)

