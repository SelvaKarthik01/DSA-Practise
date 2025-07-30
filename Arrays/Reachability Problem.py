from math import gcd
from functools import reduce

def can_reach_x(arr, x):
    base = arr[0]
    diffs = [abs(a - base) for a in arr]
    g = reduce(gcd, diffs)
    print(g)
    
    for a in arr:
        if (x - a) % g == 0:
            return "YES"
    return "NO"

# Example
arr = [1,2,5,7]
x = 18
print(can_reach_x(arr, x))  # Output: YES
