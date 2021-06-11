
result = ''

for row in range(0,7):
    for col in range(0,7):
        if (((col ==0 or col ==6)and row !=0) or ((col !=1 or col !=5 )and row ==3) ):
            result = result+'*'
        else:
            result = result+' '
    result = result+'\n'

print(result)