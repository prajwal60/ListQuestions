# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

sample = ['p','q']
result = []
for i in range(1,6):
    for j in sample:
        a=j+str(i)
        result.append(a)

print(result)

#Another Method

new_list = ['{}{}'.format(x,y) for y in range(1,6) for x in sample]
print(new_list)