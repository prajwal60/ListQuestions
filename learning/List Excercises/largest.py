# Write a Python program to get the largest number from a list.
numbers = [99,88,75,68,49,32,98]
largest = numbers[0]
for num in numbers:
    if largest<num:
        largest=num
print(f'The largest number is {largest}')