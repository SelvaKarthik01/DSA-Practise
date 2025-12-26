# Find out the Prime Numbers uptil n 
#Seive basically removes all the fatcors of the prime numbers instead of checking it again and again to reduce the time complexity 
#Seive of Erasthumus
"""
Docstring for Numbers.Seive of Eratosthenes - Prime numbers

Time Complexity : O(Nlog(logN)) -> Prime Harmonic Series
Space Complexity : O(1)
"""
import math 
n = int(input("Enter the Number N : "))
sieve = [True]*(n+1)
sieve[0]=sieve[1]=False
for i in range(2,int(math.sqrt(n)+1)):
    j = i*i 
    while(j <= n):
        sieve[j]=False 
        j += i
L = []
for i in range(len(sieve)):
    if sieve[i]:
        L.append(i)
print(L) 
    
    

            