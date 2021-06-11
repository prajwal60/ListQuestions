#  Write a Python program to calculate a dog's age in dog's years.

year = float(input('Enter your dogs year '))
age =0
if year <0:
    print("Age must be positive")
elif year <=2:
    age = year*10.5
elif year >2:
    total= year-2
    age = (total*4)+21 

print("The age of your dog is ",age)