# Write a Python program to sum of the first n positive integers.
n = int(input('Enter any positive number '))

sum = 0
for i in range(n+1):
    sum +=i 

print('The sum is ',sum)