# Write a Python program to find common items from two lists.

list1 = [1,5,9,7,3,0]
list2 = [2,4,8,6,5,7]
common = []
for i in list1:
    if i in list2:
        common.append(i)

print(common)

#Alternative method

print(set(list1) & set(list2))