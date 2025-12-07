# To Check if an array is sorted or not using recursion 
L = eval(input("Enter the List : "))
def recursion(L,i,prev_el):
    if i == len(L):
        return True 
    if prev_el <= L[i]:
        return recursion(L,i+1,L[i])
    else:
        return False
print(recursion(L,0,float("-inf")))