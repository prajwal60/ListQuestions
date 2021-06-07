# Generate and print a list of first and last 5 elements where the values are square of numbers between two numbers

Items = []

for num in range(1,31):
    Items.append(num**2)
print(f'First five elements are {Items[:5]}')
print(f'Last five elements are {Items[-5:]}')
