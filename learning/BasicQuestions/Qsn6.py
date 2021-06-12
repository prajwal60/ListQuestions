# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

simple_list = input('Enter comma seperated number').split(',')

list1 = list(simple_list)
tuple1 = tuple(simple_list)
print("list = ",list1)
print('Tiple = ',tuple1)