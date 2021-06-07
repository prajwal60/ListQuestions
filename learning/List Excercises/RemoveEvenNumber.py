# Write a Python program to print the numbers of a specified list after removing even numbers from it.

numbers = [1,5,3,4,9,7,6,5,2,0]
odd = []
for num in numbers:
    if num %2 !=0:
        odd.append(num)

print((f'Remaining odd numbers are {odd}'))


#Another  Method to complete this problem
numbers = [1,5,3,4,9,7,6,5,2,0]

numbers = [x for x in numbers if x%2!=0]
print(numbers)