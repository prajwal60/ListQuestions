# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

Items = []

for num in range(1,31):
    Items.append(num**2)

print((f'All Element except first five are {Items[5:]}'))
