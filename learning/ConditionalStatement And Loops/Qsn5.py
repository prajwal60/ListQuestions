# Write a Python program that accepts a word from the user and reverse it.

word = input('Enter a word')
reverse = ''
for i in word:
    reverse = i+reverse
print(reverse)