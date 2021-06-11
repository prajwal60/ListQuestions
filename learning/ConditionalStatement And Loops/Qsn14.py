# Write a Python program that accepts a string and calculate the number of digits and letters.

word = input('Enter any word')
string = 0
number = 0
for i in word:
    if i.isdigit():
        number +=1
    elif i.isalpha():
        string +=1
    else:
        pass

print(number)
print(string)