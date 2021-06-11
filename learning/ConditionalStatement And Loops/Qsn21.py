# Write a Python program to print alphabet pattern 'L'

result = ''
for row in range(0,7):
    for col in range(0,7):
        if ((col ==0)or row == 6):
            result = result + '*'
        else:
            result = result+' '
    result = result+ '\n'

print(result)