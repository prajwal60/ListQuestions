# Write a Python program to insert an element before each element of a list.
color = ['Red', 'Green', 'Black']
res = []



for col in color:
    for rag in ("c",col):
        res.append(rag)

print(res)