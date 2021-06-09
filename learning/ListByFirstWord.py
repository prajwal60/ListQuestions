
from itertools import groupby
from operator import itemgetter
list1 = ['Mango','Orange','Apple','Banana','Grapes','Carroz','Carrou','Cauliflower','Appy']

for letter,word in groupby(sorted(list1),key=itemgetter(0)):
    print(letter)
    for name in word:
        print(name)