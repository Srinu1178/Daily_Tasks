# Problem 4: Battery Check
# Task: Print Power Saving Mode if battery is below 20%; otherwise Normal Mode.
# Example Input:
# 18
# Example Output:
# Power Saving Mode
battery=int(input("Enter the battery percentage: "))
if battery<20:
    print("Power Saving Mode")
else:
    print("Normal Mode")