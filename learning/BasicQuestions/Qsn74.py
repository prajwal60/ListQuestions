# Write a Python program to hash a word.
word = input('Enter any word ')

changer = [1,2,3,4,5,6,2,3,1,0,4,5,0,2,1,7,6,9,4,5,7,8,6,4,9,3]

word = word.upper()

coded = word[0]

for i in word[1:len(word)]:
    i= 65-ord(i)
    coded = coded+str(changer[i])

print(coded)
