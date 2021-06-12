# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_1000(n):
    return ((abs(1000-n) <=100) or (abs(2000-n )<=100))

print(near_1000(1900))