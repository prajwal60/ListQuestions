# Write a Python program to select an item randomly from a list.
import random
sample = [1,8,6,4,7,9,3]
a = random.randint(0,6)
print(f'The random value from list is {sample[a]}')


# Another way for different type of list
list1 = ['Prajwal','Sita','Gita','Radhika','Ram']

b = random.choice((list1))
print(b)