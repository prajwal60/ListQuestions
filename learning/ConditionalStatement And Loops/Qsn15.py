# Write a Python program to check the validity of password input by users.
import re

password = input('Enter your password ')

x = True
while x:
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[0-9]",password):
        break
    elif not re.search("[@#$]",password):
        break   
    else:
        print("Valid Password")
        x =False
        break
if x:
    print('Not a valid Password')
