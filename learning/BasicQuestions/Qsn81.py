# Write a Python program to concatenate N strings
n = int(input('Enter lenth of n'))
add = ''
for i in range(n):
    str = input('Enter string to concatenate')
    add +=str
print('The concatenated string is ',add)


colours = ['Red','Black','Blue']

print('-'.join(colours))