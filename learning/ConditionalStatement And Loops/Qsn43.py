# Write a Python program to create the multiplication table (from 1 to 10) of a number.
num = int(input('Enter a number'))
prod = 1
for i in range(1,11):
    prod = num*i
    print(f'{num} x {i} = {prod}')