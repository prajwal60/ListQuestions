# Write a Python program to print alphabet pattern 'E'

result = ''

for row in range(0,7):
    for col in range(0,7):
        if ((col == 0)or ((row == 0 )or (row ==6) or ( row == 3 and col !=6)) ):
            result = result + '*'
        else:
            result = result + ' '
    result = result + '\n'
 
print(result)