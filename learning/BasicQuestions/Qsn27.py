# Write a Python program to concatenate all elements in a list into a string and return it.

def concat(a):
    res = ''
    for i in a:
        res = res+str(i)
    return res

print(concat(["a",2,'s',4,5]))