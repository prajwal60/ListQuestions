# Write a Python program to convert list to list of dictionaries.
Name =["Black", "Red", "Maroon", "Yellow"]
Code =["#000000", "#FF0000", "#800000", "#FFFF00"]

print([{'Color_Name':f,'Color_code':c} for f,c in zip(Name,Code)])