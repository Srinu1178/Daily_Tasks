'''1. Find the First Peak
Task:
A sequence contains daily website visitors. Find the first day whose visitor count is greater than both the
previous and next day. Do not check the first and last elements.
Example Input:
visitors = [120, 150, 140, 180, 200, 170, 160]
Example Output:
First peak: 150
'''
visitors = [120,150,140,180,200,170,160]
for i in range(1,len(visitors)):
    if i < len(visitors)-1:
        if visitors[i]>visitors[i-1] and visitors[i]>visitors[i+1]:
            print(f'First peak: {visitors[i]}')
            break
''' 2. Running Balance Monitor
Task:
You have a starting bank balance. Each number is a transaction. Positive means deposit and negative
means withdrawal. After every transaction, print 'Overdrawn' if balance is negative, 'Empty' if it is zero,
otherwise print the balance.
Example Input:
balance = 1000
transactions = [500, -300, -1200, 800]
Example Output:
1500
1200
Overdrawn
400 '''

balance = 1000
transaction = [500,-300,-1200,800]
for trans in transaction:
    balance += trans
    if balance<0:
        print("Overdrawn")
    elif balance == 0:
        print("Empty")
    else:
        print(balance)
''' 3. Longest Increasing Streak
Task:
Given daily temperatures, find the length of the longest consecutive increasing streak. If today's
temperature is greater than yesterday's, increase the current streak. Otherwise reset it.
Example Input:
temperatures = [20, 22, 25, 21, 23, 26, 28, 24]
Example Output:
Longest increasing streak: 4 '''

temperatures = [20, 22, 25, 21, 23, 26, 28, 24]
current = 1
longest = 1
for temp in range(1,len(temperatures)):
    if temperatures[temp]>temperatures[temp-1]:
        current+=1
    else:
        current = 1
    if current>longest:
        longest = current 
print(f'Longest increasing streak:{longest}')
''' 4. Digit Position Analyzer
Task:
Given a number, examine each digit from left to right. If the digit is greater than 5, add its position to score.
If the digit is exactly 5, add 5. Otherwise subtract 1. Positions start from 1.
Example Input:
number = 75824
Example Output:
Score: 9 '''

number = 75824
position=len(str(number))+1
score = 0
while number > 0:
    position-=1
    rem = number%10
    if rem > 5:
        score +=position
    elif rem == 5:
        score+=rem
    else:
        score-=1
    number //=10
print(f'Score: {score}')
''' 5. Temperature Change Detector
Task:
Compare each temperature with the previous one. Increase → add 2 to score. Decrease → subtract 1.
Same → add 0. At the end, score > 5 means 'Rapidly Increasing', score < 0 means 'Mostly Decreasing',
otherwise 'Stable'.
Example Input:
temperatures = [20, 25, 25, 30, 28, 35]
Example Output:
Score: 5
Stable '''
temperatures = [20, 25, 25, 30, 28, 35]
score = 0
for temp in range (1,len(temperatures)):
    if temperatures[temp]>temperatures[temp-1]:
        score+=2
    elif temperatures[temp]==temperatures[temp-1]:
        score+=0
    else:
        score-=1
print(score)
if score > 5:
    print('Rapidly Increasing')
elif score < 0:
    print('Mostly Decreasing')
else:
    print("Stable")

'''6. Alternating Transaction Detector
Task: A transaction list contains positive deposits and negative withdrawals. 
Check whether transactions strictly alternate between deposit and withdrawal.
If two consecutive transactions have the same type, the pattern is broken. 
Example Input: transactions = [500, -200, 300, -100, 700, -50]
 Example Output: Pattern is alternating '''

transaction = [500,-200,300,-100,700,-50]
found = True
for i in range(0,len(transaction)-1,2):
    if transaction[i]>0 and transaction[i+1]<0:
        found = True
    else:
        found = False
        break
if found:
    print("Pattern is alternating")
else:
    print("Pattern is broken")


'''7. Modified FizzBuzz Counter Task: Loop from 1 to 50. 
Divisible by both 3 and 5 → add 15 to score. 
Divisible only by 3 → add 3. Divisible only by 5 → add 5. 
Otherwise → add 1. Print the final score.
Example Input: No input required (process numbers 1 through 50).
Example Output: Score: 85'''

score = 0
for i in range(1,51):
    if i%3 == 0 and i%5==0:
        score += 15
    elif i%3 == 0:
        score += 3
    elif i%5 == 0:
        score += 5
    else:
        score+=1
print(f'Score:{score}')


''' 
8. Find the Largest Gap Task: Given a sequence, 
calculate the difference between every two consecutive 
numbers and find the largest absolute gap. Do not use abs(). 
Example Input: numbers = [10, 17, 5, 20, 14] 
Example Output: Largest gap: 15
'''
numbers = [10,17,5,20,14]
largest_gap = 0
for num in range(1,len(numbers)):
    gap = numbers[num]-numbers[num-1]
    if gap<0:
        gap=gap*-1
    if gap>largest_gap:
        largest_gap = gap
print(f'Largest gap: {largest_gap}')


'''9. Robot Movement Tracker 
Task: A robot starts at position 0. Positive commands move right, 
negative commands move left, and zero means no movement.
 After every command, print 'Right Zone' if position > 10, 
 'Left Zone' if position < -10, otherwise 'Safe Zone'.
   Example Input: commands = [5, 8, -4, -15, 6]
 Example Output: Safe Zone Right Zone Safe Zone Left Zone Safe Zone'''

commands = [5, 8, -4, -15, 6]

position = 0

for pos in range(len(commands)):
    position = position + commands[pos]

    if position > 10:
        print("Right Zone")
    elif position < -10:
        print("Left Zone")
    else:
        print("Safe Zone")


'''
10. Stock Price Trend Task: Compare each day's stock price with the
 previous day. Increase → trendScore +1; decrease → trendScore -1;
   same → 0. At the end, score > 2 → 'Bullish', score < -2 → 'Bearish',
     otherwise → 'Neutral'. 
     Example Input: prices = [100, 105, 103, 110, 115, 112, 120] 
     Example Output: Trend Score: 3 Bullish
'''

prices = [100, 105, 103, 110, 115, 112, 120]

trendScore = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        trendScore += 1
    elif prices[i] == prices[i - 1]:
        trendScore += 0
    else:
        trendScore -= 1

if trendScore > 2:
    print(f"Trend Score: {trendScore} Bullish")
elif trendScore < -2:
    print(f"Trend Score: {trendScore} Bearish")
else:
    print(f"Trend Score: {trendScore} Neutral")




