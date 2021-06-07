# Write a Python program to multiplies all the items in a list
numbers = [2,5,8,7,4,1,3,6,9]
total_multiply = 1
for num in numbers:
    total_multiply*=num
print(f'The product of the items in list is {total_multiply}')