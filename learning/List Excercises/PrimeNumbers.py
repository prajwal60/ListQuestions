#Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.

non_prime=[]
prime = []
for i in range(2,101):
    if i not in non_prime:
        prime.append(i)
        for j in range(i*i,101,i):
            non_prime.append(j)

non_prime.sort()
prime.sort()

set1 = set(non_prime)
print(prime)
print(set1)

