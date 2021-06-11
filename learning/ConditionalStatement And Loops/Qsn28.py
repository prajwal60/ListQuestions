# Write a Python program to print alphabet pattern 'U'.

result = ''
for row in range(0,7):
    for col in range(0,7):
        if ((col ==0 or col ==6)and (row !=6) or (row ==6)and(col>1 and col<5)):
            result = result+'*'
        else:
            result = result+' '
    result = result+'\n'
print(result)