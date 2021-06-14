# Write a Python program to get the ASCII value of a character.

letter = input('Enter any letter ')

letter = letter.upper()
letter1 = letter.lower()
print('In uppercase',ord(letter))
print('In lowercase',ord(letter1))