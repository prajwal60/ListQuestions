# Write a python program to check whether two lists are circularly identical.

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

#Manual Version
obj = ''
for i in list2:
    obj += str(i)

list11 = ''
for y in list1:
    list11 += str(y)

aa = list11 in obj*2
print(aa)

# map Version

bb = ''.join(map(str, list1)) in ''.join(map(str,list2*2))
print(bb)

cc = ''.join(map(str,list1)) in ''.join(map(str,list3*2))
print(cc)
