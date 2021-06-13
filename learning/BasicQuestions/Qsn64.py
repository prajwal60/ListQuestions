# Write a Python program to get file creation and modification date/times.
import os.path,time
print('Last modified: %s'%time.ctime(os.path.getmtime('main.txt')))
print('Created on : %s'%time.ctime(os.path.getctime('main.txt')))