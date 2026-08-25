# Problem 18: Compare Ends
# Task: If first and last chars equal print Palindrome Ends.
# Example Input:
# level
# Example Output:
# Palindrome Ends
word = input('Enter the word: ')
if word[0]==word[-1]:
    print("Palindrome Ends")
else:
    print("Not Palindrome")