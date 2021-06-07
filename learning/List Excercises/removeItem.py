# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
sample.pop(5)
sample.pop(4)
sample.pop(0)
print(f'The list after removing item from list are {sample}')


