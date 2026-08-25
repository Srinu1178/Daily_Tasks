# Problem 2: Storage Limit
# Task: Print Space Available if used space is below 64 GB; otherwise Storage Full.
# Example Input:
# 52
# Example Output:
# Space Available
storage = int(input("Enter the storage:"))
if storage<=64:
    print("Space Available")
else:
    print("Storage Full")