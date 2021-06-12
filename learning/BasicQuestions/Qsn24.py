# Write a Python program to test whether a passed letter is a vowel or not.

letter = input('Enter any letter')

if letter.lower() in ('a','e','i','o','u'):
    print('Its Vowel')
else:
    print('Its consonent')