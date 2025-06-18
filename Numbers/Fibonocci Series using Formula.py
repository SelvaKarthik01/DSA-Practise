n = int(input("Enter the Number N : "))
import math 
def fibonocci_formula(n):
    ans = (1/math.sqrt(5))*((((1 + math.sqrt(5))*0.5)**n) - (((1 - math.sqrt(5))*0.5)**n))
    return int(ans)
for i in range(1,n+1):
    print(fibonocci_formula(i),end = " ")
