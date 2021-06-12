# Write a Python program to display astrological sign for given date of birth
day = int(input('Enter your birth date'))
month = input('Enter your birth month')

if (month == 'March' and day >= 21) or (month == 'April' and day<=20):
    sign = 'Aries'
elif (month == 'April' and day >= 21) or (month == 'May' and day<=20):
    sign = 'Taurus'
elif (month == 'May' and day >= 21) or (month == 'June' and day<=21):
    sign = 'Gemini'
elif (month == 'June' and day >= 22) or (month == 'July' and day<=22):
    sign = 'Cancer'
elif (month == 'July' and day >= 23) or (month == 'August' and day<=22):
    sign = 'Leo'
elif (month == 'August' and day >= 23) or (month == 'September' and day<=22):
    sign = 'Virgo'
elif (month == 'September' and day >= 23) or (month == 'October' and day<=22):
    sign = 'Libra'
elif (month == 'October' and day >= 23) or (month == 'November' and day<=22):
    sign = 'Scorpio'
elif (month == 'November' and day >= 23) or (month == 'December' and day<=21):
    sign = 'Sagittarius'
elif (month == 'December' and day >= 22) or (month == 'January' and day<=20):
    sign = 'Capricorn'
elif (month == 'January' and day >= 21) or (month == 'February' and day<=18):
    sign = 'Aquarius'
elif (month == 'February' and day >= 19) or (month == 'March' and day<=20):
    sign = 'Pieces'

print('Your sign is ',sign)