word = 'python is easy and python is powerful'

freq={}
current_word = ""
for char in word:
    if char!=" ":
        current_word+=char
    elif current_word:
        freq[current_word]=freq.get(current_word,0)+1
        current_word=""
if current_word:
    freq[current_word] = freq.get(current_word, 0) + 1
print(freq)


# 7. Find Duplicate Values
# Given:
# numbers = [10, 20, 30, 20, 40, 10, 50, 30]
# Output:
# 10
# 20
# 30
# Try solving it without using set() first.
numbers = [10, 20, 30, 20, 40, 10, 50, 30]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]==numbers[j]:
            print(numbers[i])

# 8. Remove Duplicates

# Input:

# numbers = [10, 20, 10, 30, 20, 40]

# Output:

# [10, 20, 30, 40]

# Don't use:

# set()

nums = [10, 20, 10, 30, 20, 40]
print("Remove Duplicates")
i=0
while i<len(nums):   
    j = i+1       
    while j<len(nums):
        if nums[j]==nums[i]:
            nums.pop(j)
        j+=1
    i+=1

print(nums)

# 9. Second Largest Number
# Given:
# numbers = [10, 50, 20, 80, 60, 80]
# Find the second largest unique number.
# Expected:
# 60
# Don't simply use:
# sort()
print("Second Largest element: ")

numbers = [10, 50, 20, 80, 60, 80]
largest = float('-inf')
sec_largest = numbers[0]
for ele in numbers:
    if ele>largest:
        largest = ele
for ele in numbers:
    if ele>sec_largest and ele<largest:
        sec_largest=ele

print(sec_largest)

# 10. Search Product
# Create:
# products = ["laptop", "mobile", "tablet", "watch", "keyboard"]
# Ask the user for a product.
# Output:
# Product available
# or
# Product not available

products = ["laptop", "mobile", "tablet", "watch", "keyboard"]
user_product = input("Enter the product: ").lower()
if user_product in products:
    print("Product available")
else:
    print("Product not available")

