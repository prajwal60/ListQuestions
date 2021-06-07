# Write a Python program to find the second largest number in a list.

sample=[17,1,1,1,1,1,1,1]
sample.sort()
smallest = sample[0]
for num in sample:
    if num>smallest:
        smallest=num
        print(f'The second smallest is {smallest}')
        break
    
else:
    print('None')

