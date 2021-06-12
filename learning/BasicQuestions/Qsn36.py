# Write a Python program to add two objects if both objects are an integer type.

def sum(a,b):
    if not (isinstance(a,int) and isinstance(b,int)):
        return "Input must be  integer"
    else:
        return a+b

print(sum(int(input('Enter first number')),int(input('Enter second number'))))