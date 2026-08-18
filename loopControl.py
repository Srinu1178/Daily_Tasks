for i in range(1,11):
    print(i)
    if i==5:
        print(f'{i} found')
        break


# wap to print that bread is found if bread is in the list of items
target = input("Enter the item you are looking for: ")
items = ["jam","butter","milk","bread","eggs","cookies","cool drinks"]
for item in items:
    if item==target:
        print(f'{target} found')
        break
else:
    print(f'{target} not found')

#WAP to check whether a number greater than 50 exists in a list or not
list1 = [24,45,21,33,49,51,79,90]
for num in list1:
    if num>50:
        print(f'{num} which is greater than is found')
        break
else:
    print("No number is greater than 50")

# check wheather admin has loggin in today or not

todayLogins=['dev0101','tester1111','designer110','admin001','mana898','teamlead']
i= 0
j = len(todayLogins)
while i<j:
    if todayLogins[i]=='admin001':
        print("admin login in today")
        break
    i+=1
else:
    print("admin doesnot login today")


# WAP to enter valid pin of your atm card upto 3 attempts
pin = "9988"
i = 1
while i<=3:
    user_pin=input("Enter the pin no: ")
    if user_pin==pin:
        print("Account details displayed")
        break
    i+=1
else:
    print("too many attempts")
    print("Card is blocked")











