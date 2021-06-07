# Write a Python program to find the list of words that are longer than n from a given list of words.
n= 3
sample = ['Prajwal','Sagar','Amrit','Amy','Ram','Shyam']
NameList = []
for item in sample: 
    if len(item)>n:
        NameList.append(item)

print(f'The list of words that are longer than n are {NameList}')
    