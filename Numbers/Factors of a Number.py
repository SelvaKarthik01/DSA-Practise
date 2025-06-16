# To Find the Factors of a number Efficiently
n = int(input("Enter the Number : "))
L = []
import math
for i in range(1,int(math.sqrt(n)+1)):
    if n % i == 0 :
        L.append(i)
        L.append(n // i)
L.sort()
print(L)