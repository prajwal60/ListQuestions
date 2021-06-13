# Write a Python program to get an absolute file path.
def AbsulutePath():
    from os import path
    return path.abspath('file is here')

print('Absolute Path is ',AbsulutePath())
