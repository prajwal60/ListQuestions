# Write a Python program to change the position of every n-th value with the (n+1)th in a list.

list1 = [0,1,2,3,4,5]
result = [list1[0]]
for i in range(1,len(list1)):
    if i%2!=0:
        result.insert(i-1,list1[i])
    else:
        result.insert(i,list1[i])


print(result)


