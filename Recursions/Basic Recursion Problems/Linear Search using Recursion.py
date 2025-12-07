# To perform Linear Search using Recursion 

L = eval(input("Enter the List : "))
target = int(input("Enter the target : "))
def linear_search(L,target,index):
    if target == L[index]:
        return True
    if index == len(L)-1:
        return False
    return linear_search(L,target,index+1)
print(linear_search(L,target,0))