# Write a Python program to remove duplicates from a list. 

sample = [2,4,6,1,8,3,2,6,8,7]
result = []
for num in sample:
    if num not in result:
        result.append(num)

print(f'The list after removing duplicates is {result}')
