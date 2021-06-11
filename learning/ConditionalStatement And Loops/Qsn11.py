#  Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

row = int(input("Enter row"))
col = int(input("Enter col"))

matrix = [[x*y for x in range(0,col)]for y in range(0,row)]
print(matrix)