# Write a Python program to calculate the sum of the digits in an integer.
number= int(input('Enter any number'))

print(type(number))
sum1 = 0
for i in str(number):
    sum1 +=int(i)
print("The sum of giver integer is" ,sum1)

