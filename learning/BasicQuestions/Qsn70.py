# Write a Python program to sort files by date.
import glob
import os
files = glob.glob('BasicQuestions/*.py')
files.sort(key=os.path.getmtime)

print('\n'.join(files))