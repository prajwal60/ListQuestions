# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
num = int(input('Enter any number'))
if num%2 ==0:
    value ='Even'
else:
    value = 'Odd'

print("Entered number is ",value)