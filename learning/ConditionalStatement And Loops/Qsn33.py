# Write a Python program to convert month name to a number of days
month = input("Enter any month ")

if month.upper() == 'FEBRUARY':
    print(F'{month} has 28/29 days')
elif month.upper() in ("APRIL", "JUNE", "SEPTEMBER", "NOVEMBER"):
    print(F'{month} has 30 days')
elif month.upper() in ("JANUARY", "MARCH", "MAY", "JULY", "AUGUST", "OCTOBER", "DECEMBER"):
    print(F'{month} has 31 days')

else:
    print("Please spell it correctly")