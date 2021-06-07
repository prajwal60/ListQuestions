# Write a Python program to generate all permutations of a list in Python.
import itertools
#Providing default list 
print(list(itertools.permutations([1,2,3,4])))

#Providing non default list
li = []
for i in range(5):
    li.append(i)
print(list(itertools.permutations(li)))
