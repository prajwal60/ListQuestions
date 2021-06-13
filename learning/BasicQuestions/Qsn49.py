# Write a Python program to list all files in a directory in Python.
from os import listdir
from os.path import join,isfile

file_list = [x for x in listdir('/home/prajwal/Desktop/Learning/Python/ListQuestions/learning/BasicQuestions') if isfile(join('/home/prajwal/Desktop/Learning/Python/ListQuestions/learning/BasicQuestions',x),)]
print(file_list)