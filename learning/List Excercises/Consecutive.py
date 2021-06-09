# Write a Python program to generate groups of five consecutive numbers in a list.

list1 = [[[5*i+j+k for j in range(1,6)] for i in range(5)] for k in range(5)]
print(list1)

