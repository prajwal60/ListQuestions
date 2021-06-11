# Write a Python program to print alphabet pattern 'G'.

result = ''
for row in range(0,7):
    for col in range(0,7):
        if ((col ==0) and (row !=0 and row !=6) or ((row ==0 or row == 6) and (col>0 and col<6))or ((row ==1 or row == 5 or row == 4)and (col ==6))or ((row ==3)and ((col!=2)and col!=1))):
            result = result+'*'
        else:
            result = result+' '
    result=result+'\n'
print(result)