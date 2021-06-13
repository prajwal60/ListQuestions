# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
principal = float(input('Enter Principal amount '))
rate = float(input('Enter rate interest '))
time = float(input('Enter time interval'))
r = rate/100

final_value = principal*(1+(r/1))**time
print("The compound interest is ",round(final_value,2))