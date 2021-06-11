# Write a Python program to print alphabet pattern 'X'.

result = ''

for row in range(0,7):
    for col in range(0,6):
        if ((col ==0 or col ==5)and (row !=2 and row !=3 and row!=4)or(row ==2 or row ==4)and (col == 1 or col == 4) or (row ==3)and (col==3 or col ==2)):
            result = result+'*'
        else:
            result=result+' '
    result = result+'\n'
print(result)