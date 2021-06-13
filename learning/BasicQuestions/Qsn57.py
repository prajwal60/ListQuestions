# Write a Python program to get execution time for a Python method.

import time
def sum():
    starttime = time.time()
    sum = 0
    for i in range(1,5):
        sum +=i
    endtime = time.time() 
    return sum,endtime-starttime

print(sum())
