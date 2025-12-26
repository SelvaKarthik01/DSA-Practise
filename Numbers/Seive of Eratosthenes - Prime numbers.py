# Find out the Prime Numbers uptil n 
#Seive basically removes all the fatcors of the prime numbers instead of checking it again and again to reduce the time complexity 
#Seive of Erasthumus
n = int(input("Enter the Number : "))
import numpy as np
L = np.zeros(n+1)
ans = []
def factors(a,n,L):
    i = 2
    while(a*i < n+1):
        L[a*i] = -1
        i += 1

for i in range(2,n+1):
    if L[i] != -1:
        L[i] = 1
        ans.append(i)
        factors(i,n,L)
print(ans)

            