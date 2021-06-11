#  Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.

data = input('Number').split(',')
print(data)
for i in data:
    if int(i)%5==0:
        print(i)
