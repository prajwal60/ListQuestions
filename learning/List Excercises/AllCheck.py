# Write a Python program to check whether all items of a list is equal to a given string.

color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c == 'green' for c in color2))

for i in color2:
    print(all(i=='green'))
