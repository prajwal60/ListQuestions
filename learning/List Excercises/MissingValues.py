# Write a Python program to find missing and additional values in two lists.
#For both Integer and string
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
missing = set(list1)-set(list2)
additional = set(list2)-set(list1)
print(f'Missing : {missing}')
print(f'Additional : {additional}')

#Another Method for string
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print(','.join(set(list1).difference(list2)))
print(','.join(set(list2).difference(list1)))