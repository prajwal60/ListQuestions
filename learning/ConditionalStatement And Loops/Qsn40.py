# Write a Python program to find the median of three values.
num1 = int(input('Enter first Value'))
num2 = int(input('Enter first Value'))
num3 = int(input('Enter first Value'))
if num1<num2:
    if num2<num3:
        median = num2
    elif num3<num2:
        median = num3
elif num2<num1:
    if num1<num3:
        median = num1
    elif num3<num1:
        median = num3
else:
    median = num3

print(median)
