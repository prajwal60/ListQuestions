# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

item = input("Enter any thing")
res = ''
for i in item:
    res += i.lower()

print(res)
