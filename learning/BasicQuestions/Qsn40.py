#  Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

x1 = int(input('Enter value of x1 '))
x2 = int(input('Enter value of x2 '))
y1 = int(input('Enter value of y1 '))
y2 = int(input('Enter value of y2 '))

distance = ((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f'Distance between points ({x1}, {x2}) and ({y1}, {y2}) is ',round(distance,4))