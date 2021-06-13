# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
feet = float(input('Enter distance in feet '))

print('Inches into inches = ',feet*12)
print('Inches into mile = ',round(feet/5280,2))
print('Inches into yard = ',round(feet/3,2))