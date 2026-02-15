"""
Docstring for Numbers.Count Primes in Range of L to R

Time Complexity : O(n) -> for Creating Sieve Array + O(nlog(logn)) -> Prime Harmonic Series
Space Compleixty : O(n) -> for Storing the Sieve Array 
"""


def soe(n):
    sieve = [1]*(n+1) #O(n)
    sieve[0]=sieve[1] = 0 
    prefix_sum  = 0
    for i in range(2,n+1): # O(nlog(logn))
        if sieve[i] == 1:
            prefix_sum += 1
            sieve[i] = prefix_sum 
            mul = i 
            while(i*mul <= n):
                sieve[i*mul] = 0 
                mul += 1
        else:
            sieve[i] = prefix_sum 
    return sieve 


l = int(input("Enter the L bound Number : "))
r = int(input("Enter the R bound Number : "))
sieve = soe(r)
print(f"Number of Primes Numbers Between L-{l} and R-{r} : ",sieve[r]-sieve[l-1]) # l-1 for being inclusiev of 3 
                
            