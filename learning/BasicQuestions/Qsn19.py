# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
new_string = input('Enter any thing ')

def stringAdder(a):
    oe = a[:2]
    if oe.upper() =='IS':
        return a
    else:
        return 'Is'+a

print(stringAdder(new_string))