# Write a Python program to accept a filename from the user and print the extension of that.

filename = input('Enter the file name with extension')
extension = filename.split('.')

print('The extension of given file name is ',extension[-1])

