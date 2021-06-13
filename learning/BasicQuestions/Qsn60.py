#  Write a Python program to calculate the hypotenuse of a right angled triangle.
from math import sqrt

perp = float(input('Enter perpendicular of triangle'))
base = float(input('Enter base of triangle'))

height = sqrt(perp**2 + base**2)
print('Height = ',height)