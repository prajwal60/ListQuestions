# Write a Python program to get the Fibonacci series between 0 to 50.
a=0
b=1
print(a)
print(b)
for i in range(10):
    c = a+b
    a=b
    b=c
    if c >50:
        break
    print(c)
