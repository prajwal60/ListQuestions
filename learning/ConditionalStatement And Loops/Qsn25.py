# Write a Python program to print alphabet pattern 'R'.

result = ''
for row in range(0,7):
    for col in range(0,7):
        if ((col==0)or (row ==0 or row ==3)and (col !=6) or (row ==1 or row ==2)and (col==6) or (row ==4)and (col ==2) or (row ==5)and (col ==4) or (row ==6)and (col ==6)):
            result = result+'*'
        else:
            result = result+' '
    result = result+'\n'
print(result)