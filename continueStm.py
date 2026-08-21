# list1=[45,63,12,-11,0,60,32,122,90]
# i = 0
# while i<len(list1):
#     value = list1[i]
#     i+=1
#     if value<50:
#         continue
#     print(value)

# skip all empty values in a list
# usernames = ['sumanth101','satish909','shankar232','','rajesh111','','']

# i = 0
# while i<len(usernames):
#     if len(usernames[i])==0:
#         i+=1
#         continue
#     print(usernames[i])
#     i+=1


#  # stock and its value of  stock market
# shareMarket = {
#     'SBI':350,
#     'HDFC':221,
#     'ASIAN':440,
#     'EMARELD': 1010,
#     'BOEING': 110
# }
# companies = list(shareMarket)
# i = 0
# while i < len(companies):
#     name = companies[i]
#     i+=1
#     if shareMarket[name]<440:
#         continue
#     print(companies[i])


# print result of student based on his marks
marks = {
    'Durgasri':98,
    'Rasagnya':76,
    'Venkat':32,
    'Sumanth':78,
    'bhanu Teja': 89,
    'Shankar': 31
}
# 'Durgasri':"passed'

person_names = list(marks.keys())
i = 0
while i <len(person_names):
    name = person_names[i]
    i+=1
    if marks[name]<36:
        continue
    print(f'{name} : passed')








