# Write a Python program to calculate body mass index.
height = float(input('Enter your height in feet'))
weight  = float(input('Enter your weight in kilogram '))

bmi = weight/height**2
print('BMI = ',round(bmi,2))