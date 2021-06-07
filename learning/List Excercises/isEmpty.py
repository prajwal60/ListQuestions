# Write a Python program to check a list is empty or not.

sample = [1]
count = 0
for i in sample:
    count +=1
if count>0:
    print(f'There are {count} items in list')
else:
    print(f'The list is empty')