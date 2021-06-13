# Write a Python program to convert all units of time into seconds.
days = int(input('Enter days'))
hour = int(input('Enter hour'))
min = int(input('Enter minutes'))
sec = int(input('Enter seconds'))

second = days*24*60*60 + hour *60*60 + min*60 + sec
print('Total second is ',second)