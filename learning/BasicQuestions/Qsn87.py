# Write a Python program to get the size of a file.
import os

file_size = os.path.getsize('practice.py')
print('The size of the file is ',file_size,'Bytes')