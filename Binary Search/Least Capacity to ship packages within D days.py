"""
Docstring for Binary Search.Least Capacity to ship packages within D days
"""

def Binary_Search(weights,days):
    low = max(weights)
    high = sum(weights)
    def NoDays(weights,capacity):
        sum = 0 
        days = 0 
        for i in range(len(weights)):
            if sum + weights[i] <= capacity:
                sum += weights[i]
            else:
                days += 1
                sum = weights[i]
        days += 1
        return days 
    while(low<= high):
        mid = low + (high-low)//2
        if NoDays(weights,mid) <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low 
weights = eval(input("Enter the Weights : "))
days = int(input("Enter the  Threshold Days : "))
print(Binary_Search(weights,days))
