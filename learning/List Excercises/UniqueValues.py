# Write a Python program to get unique values from a list.

list1 = [1,5,6,1,9,3,4,7,9,3]
#Converting it into list
my_set = set(list1)
list2 = list(my_set)
print(list2)

#Creating using new list
l3 = []
for item in list1:
    if item not in l3:
        l3.append(item)
        l3.sort()
    
print((l3))