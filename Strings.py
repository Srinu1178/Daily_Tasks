# String : It is a group of characters enclosed by single or double quotes

str1 = "Hello World"
print(str1.upper())
# returns a copy of string with all characters in upper case

print(str1.lower())
# str1.lower(): returns a copy of string with all characters in lowecase

print(str1.swapcase())
#str1.swapcase(): returns a copy of string with all upper
# case characters converted to lowercase and vice versa

print(str1.capitalize())
# str1.capitalize(): returns a copy of string with first letter 
# captialized  and remaining to lowercase 

s="gooD morNING"
print(s.title())
#s.title: returns a copy of string with first letter in each word captialized

s1 = " Python is easy "
print(s1.strip())
#s1.strip() : returns a copy of string with leading and trailing 
# whitespace removed

print(s1.lstrip())
#s1.lstrip(): returns a copy of the string with leading space removed

print(s1.rstrip())
#s1.rstrip(): returns a copy of the string with trailing space removed

s3 = " My name :is :SRK"
#s3.split(): splits the string into a list of substring based on the
# specific delimeter
#if no delimeter is specified, then whitespace is selected as default
# delimeter

print(s3.split())

s4 ="Hello Java"
print(s4.replace('Java','Python'))

#s4.replace(): returns a copy of the string with all occurences
# of specified substring replace with another substring

#str.join():
#   -->Join a list of strings into a single string using a specified
# delimeter
print(" ".join(["Naga","Venkata","Srinivasu"]))

# str1.index(): returns the index of the first occurence of the string searched
s = "Python is very very easy"
print(s.index("very"))

#str1.find()
# --> returns the index of the first occurence of the substring in a string

print(s.find("is"))

#str.count(): returns the no.of no_overlapping occurences of a substring
#in the searched string

s3="Good Good Good Good Morning"
print(s3.count("Good"))

#str.startswith(): returns a boolean stating wheather a string start
# with the specified prefix
s = "siva123"
print(s.startswith("si"))

# str.endswith(): returns a boolean stating wheather a string start
# with the specified suffix
print(s.endswith("va12"))

# str.isalnum(): returns a boolean stating wheather a string contain only
# letter and digits

s4 = "Siva123"
print(s4.isalnum())

# str.isalpha(): returns a boolean stating wheather a string contain
#  only letters
s5 = "srinu123"
print(s5.isalpha())

# str.isdigit():returns a boolean stating wheather a string contain
#  only digits
s6 = "123"
print(s6.isdigit())

# str.islower():returns a boolean stating wheather a string is in lowercase

s6="siva123"
print(s6.islower())

# str.isupper(): returns a boolean stating wheather a string is in uppercase
s7 = "siva123"
print(s7.isupper())

#str.isspace(): returns a boolean stating wheather a string contains only
# white spaces
s8 = ' '
print(s8.isspace())

# str.title(): returns a boolean stating wheather a string is in title case
s9="Hello Bhai"
print(s9.istitle())

# str.removeprefix(): returns a string with the given prefix string is removed
#  if present
s10 = "Python"
print(s10.removeprefix('Py'))

# str.removesuffix(): 
# returns a string with the given suffix string is removed if present

s11 = "Python"
print(s11.removesuffix("ON"))
