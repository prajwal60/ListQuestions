# Write a Python program to check a triangle is equilateral, isosceles or scalene.

a =input('Enter first side of triangle')
c =input('Enter second side of triangle')
b =input('Enter third side of triangle')

if a==b==c:
    print('It is an eqiilateral Triangle')
elif a==b!=c or a==c!=b or b==c!=a:
    print('It is an iscsceles triangle')
elif a!=b!=c:
    print('It is scalene triangle')
