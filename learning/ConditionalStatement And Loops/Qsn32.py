# Write a Python program to check whether an alphabet is a vowel or consonant.

char = input('Enter any character')

if char.upper()=="A" or char.upper()=="E" or char.upper()=="I" or char.upper()=="O" or char.upper()=="U":
    print(f'{char} is vowel')
else:
    print(f'{char} is consonent') 