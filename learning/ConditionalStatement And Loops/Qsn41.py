# Write a Python program to get next day of a given date.

year = int(input('Enter a year'))
if (year % 4 == 0) or (year % 400 ==0):
    leap = True
else:
    leap =False
month = int(input('Enter a month'))
if (month in (1,3,5,7,8,10,12)):
    month_leg = 31
elif month ==2:
    if leap:
        month_leg = 29
    else:
        month_leg=28
else:
    month_leg=30
    

day = int(input('Enter a day'))
if day < month_leg:
    day +=1
else:
    day = 1
    if month ==12:
        month=1
        year +=1
    else:
        month +=1

print(f'The next date is {year}-{month}-{day}')