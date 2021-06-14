# Write a Python program to test whether all numbers of a list is greater than a certain number.
sample = [4,5,6,7,8,9,10]

mini = min(sample)
n = int(input('Enter any number '))

if mini > n:
    print("All of them in list are greater")
else:
    print('Some of them in list are smaller')


#Another Approach

sample2 = [4,5,6,7,8,9,10]
m = int(input('Enter any number'))
print(all(x>m for x in sample2))