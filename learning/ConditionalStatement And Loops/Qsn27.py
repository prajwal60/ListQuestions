# Write a Python program to print alphabet pattern 'T'
result = ''
for row in range(0,7):
    for col in range(0,7):
        if ((col==3)or (row ==0)):
            result = result +'*'
        else:
            result = result+' '
    result = result + '\n'
print(result)