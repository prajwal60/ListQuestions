# Write a Python program to check whether a string is numeric.

string = "123_56"
print(string.isdigit())

try:
    i = float(string)
    print('Is numberic')
except(ValueError, TypeError):
    print('Not a number')