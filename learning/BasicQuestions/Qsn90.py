# Write a Python program to create a copy of its own source code.

def file_cpy(src,dest):
    with open(src, 'r') as f, open(dest, 'w') as d:
        d.write(f.read())

file_cpy('Qsn90.py','copy.py')




