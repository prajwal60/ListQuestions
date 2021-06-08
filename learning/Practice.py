from itertools import combinations
list1= [10,20,30,40]
sub = []
for i in range(0,len(list1)+1):
    x =[list(x) for x in combinations(list1,i)]
    if len(x)>0:
        sub.extend(x)
print(sub)    




