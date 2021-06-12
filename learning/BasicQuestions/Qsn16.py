#  Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

num = int(input('Enter any number '))
if num >17:
    diff = num-17
    diff = diff*2
else:
    diff = 17-num
    diff = abs(diff)

print('The difference is ',diff)