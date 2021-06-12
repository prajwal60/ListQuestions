# Write a Python program to calculate number of days between two dates.
from datetime import date
date1 = date(2014,7,9)
date2 = date(2015,7,9)
diff = date2-date1
print(diff.days)