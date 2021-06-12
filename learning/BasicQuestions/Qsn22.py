# Write a Python program to count the number 4 in a given list.
list1 = [1,2,3,4,5,6,7,8,9,4,5,6,1,2,4,3,2,4,4]
c= 0
for i in list1:
    if i ==4:
        c= c+1

print('There are %i 4 in list'%c)