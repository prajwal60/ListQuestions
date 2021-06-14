# Write a Python program to count the number occurrence of a specific character in a string.
string = input('Enter any string ')
letter = input('Enter counting letter ')
count = 0
for i in string:
    if i == letter:
        count += 1
print(f'It repates {count} times')


#alternative method

print(string.count(letter))