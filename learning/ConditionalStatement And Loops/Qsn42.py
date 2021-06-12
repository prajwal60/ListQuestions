# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
print('Program to calculate the sum of n integer number')

sum = 0
x = True
while x ==True:
    num = int(input('Enter number'))
    if num==0:
        x=False
        print('Program Terminated')
    else:
        sum =sum+num
        print('Sum = ',sum)
    print('\n')
    