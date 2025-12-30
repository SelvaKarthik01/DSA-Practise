"""
Docstring for Numbers.Count the Number of Primes Before a Number

Time Complexity : O(log(logn))
Space Complexity : O(n)
"""
import math 
n = int(input("Enter the Number : "))
sieve = [1]*(n+1)

sieve[0]=sieve[1] = 0
for i in range(2,int(math.sqrt(n)+1)):
    for j in range(i*i,n+1,i):
        sieve[j] = 0 
prefix = 0 
for i in range(n+1):
    prefix = prefix + sieve[i]
    sieve[i] = prefix 
print(sieve)