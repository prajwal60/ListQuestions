# Write a Python program to convert a list of characters into a string.

list1 = ['P','Y','T','H','O','N']
obj = ''
for num in list1:
    obj += str(num)    
print(obj)

#Another Method
str1 = ''.join(list1)
print((str1))