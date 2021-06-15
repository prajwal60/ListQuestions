# Write a Python program to access and print a URL's content to the console.
from http.client import HTTPConnection
conn = HTTPConnection('www.example.com')
conn.request('Get','/')
result = conn.getresponse()
context = result.read()
print(context)