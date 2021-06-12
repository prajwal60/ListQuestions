# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))

if num1==num2:
    sum = diff = 5
else:
    sum = num1+num2
    diff = abs(num1-num2)

print('Sum is ',sum)
print('Difference is ',diff)