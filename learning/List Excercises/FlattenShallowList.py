# Write a Python program to flatten a shallow list.
import itertools
list1 = [[2,4,3],[1,5,6], [9], [7,9,0]]
newlist = list(itertools.chain(*list1))
print(newlist)