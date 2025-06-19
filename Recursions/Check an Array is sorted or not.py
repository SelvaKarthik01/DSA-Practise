# To Check if an array os sorted or not using recursion 
L = eval(input("Enter the Input : "))
def sorted(L,i):
    if i == len(L) -1:
        return True
    if L[i] > L[i+1]:
        return False
    return sorted(L,i+1)
print(sorted(L,0))