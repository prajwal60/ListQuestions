# Write a Python program to sort three integers without using conditional statements and loops.

x = int(input('Enter any number'))
z = int(input('Enter any number'))
y = int(input('Enter any number'))

mv = min(x,y,z)
mx = max(x,y,z)
mid = (x+y+z)-mv-mx
print(mv,mid,mx)