# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
num = abs(int(input('Enter desired copies ')))
string = input('Enter desired string ')

copies = num*string
print(copies)