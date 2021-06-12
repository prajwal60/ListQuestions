# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input('Enter your first name')
last_name = input('Enter your last name')

full = first_name+' '+last_name
simp = last_name+ ' '+first_name
print('Simple reverse = ', simp)
rev=''
for i in full:
    rev = i+rev

print('Complex reverse = ',rev)