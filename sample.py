n = 764532
even_sum = 0
odd_sum = 0
max_sum = 0
while n>0:
    rem = n%10
    if rem%2==0:
        even_sum+=rem
    else:
        odd_sum+=rem
    n = n//10
if even_sum>odd_sum:
    max_sum = even_sum
    print(f"{max_sum} even sum is bigger")
else:
    max_sum = odd_sum
    print(f"{max_sum} odd sum is bigger")