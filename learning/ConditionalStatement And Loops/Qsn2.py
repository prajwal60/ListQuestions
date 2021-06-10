# Write a Python program to convert temperatures to and from celsius, fahrenheit.
# celcius = float(input('Enter celcius to convert into fahrenheit'))
# fahrenheit = float(input('Enter fahrenheit to convert into celcius'))

# cel = ((fahrenheit-32)/9)*5
# fahr = ((9*celcius)/5)+32
# print(f'{celcius} celcius is {fahr} fahrenheit'.format(celcius,fahr))
# print(f'{fahrenheit} farenheit is {cel} celcius'.format(fahrenheit,cel))

value = input("Enter temperature for conversion")

degree = int(value[:-1])
check = value[-1]

if check.upper() =='F':
    print(degree,'Fahrenheit is',round(((degree-32)/9)*5),' celcius')
    
elif check.upper() =='C':
    print(degree,'Celcius is',round(((9*degree)/5)+32),' fahrenheit ')
else:
    print('Add only  f or c at last to convert')