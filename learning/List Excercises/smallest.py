# Write a Python program to get the smallest number from a list.
number = [56,84,76,23,94,12,90]
smallest = number[0]
for num in number:
    if smallest>num:
        smallest=num
print(f'The smallest number is {smallest}')