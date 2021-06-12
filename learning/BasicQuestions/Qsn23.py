# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
n = int(input('Enter n '))
string = input('Enter any string')
if len(string)<=2:
    print(string*n)
else:
    val = string[:2]
    print(val*2)  