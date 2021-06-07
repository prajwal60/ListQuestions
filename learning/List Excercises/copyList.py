# Write a Python program to clone or copy a list.
sample = [1,2,3,8,6]

#simple method to clone
copySample = list(sample)
print(f'The clone of the list is {copySample}')



#Using for loop
clone = []
for num in sample:
    clone.append(num)
print(f'The clone of the list using for loop is {clone}')