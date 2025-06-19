# To reverse a numebr using recursion 
import math
def reverse_num(n):
    if n == 0:
        return 0
    return (n%10)*(10**int(math.log(n,10))) + reverse_num(n//10)
n = int(input("Enter the Number : "))
print(reverse_num(n))

