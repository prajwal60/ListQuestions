#  Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

def Addition(a,b,c):
    if a==b==c:
        sum = a+b+c
        return sum*3
    else:
        sum = a+b+c
        return sum

print(Addition(2,3,4))