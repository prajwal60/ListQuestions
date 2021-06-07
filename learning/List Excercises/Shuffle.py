# Write a Python program to shuffle and print a specified list.
from random import shuffle

sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(sample)
print(f'The shuffled list is {sample}')