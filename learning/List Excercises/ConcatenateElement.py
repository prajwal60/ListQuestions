# Write a Python program to concatenate elements of a list.

string = ''

list1 = ['Prajwal','is',1,2,3,4,'Ghimire']

for i in list1:
    string += str(i) + ' '
print(string)


#Alternative Methof

attach = ' '.join(map(str,list1))
print(attach)