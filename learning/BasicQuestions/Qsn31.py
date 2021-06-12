# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
x = int(input('Enter first Number '))
y = int(input('Enter second number '))
if x%y ==0:
    print(y)
else:
    for i in range(int(y/2),0,-1):
        if x%i ==0 and y%i==0:
            print(i)
            break