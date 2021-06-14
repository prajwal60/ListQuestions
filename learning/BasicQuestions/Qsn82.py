# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
list1 = [4,5,6,7,8,9]
tuple1 = (4,5,6,7,8,9)
set1 = {4,5,6,7,8,9}
dist = {'a':4,'b':5,'c':9}
listsum = sum(list1)
tuplesum = sum(tuple1)
setsum = sum(set1)
distsum = 0
for i in dist:
    distsum += dist[i]


print("Sum from lisst",listsum)
print("Sum from Tuple",tuplesum)
print("Sum from Set",setsum)
print("Sum from Dictionary",distsum)
    