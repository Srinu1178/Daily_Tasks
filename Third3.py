# Problem 3: Train Arrival
# Task: Print Late if delay is greater than 10 minutes; otherwise On Time.
# Example Input:
# 14
# Example Output:
# Late
time = int(input("Enter the minutes: "))
if time>10:
    print("Late")
else:
    print("On Time")