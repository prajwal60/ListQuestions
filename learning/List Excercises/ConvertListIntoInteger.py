# Write a Python program to convert a list of multiple integers into a single integer.

from typing import List


list1 = [11, 33, 50]
strList = ''
for i in list1:
    strList += str(i)
print(int(strList))

#Alternate Method

strList1 = int(''.join(map(str,list1)))
print(strList1)