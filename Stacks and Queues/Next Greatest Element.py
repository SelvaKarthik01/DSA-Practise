# Monotonic Stack 
# Ex -> [6,0,8,1,3]
# Output -> [8,8,-1,3,-1]
 
L = eval(input("Enter the List : "))
n = len(L)
stack = []
ans = [-1] * n

for i in range(n - 1, -1, -1):
    # Pop all elements <= current, they cannot be next greater
    while stack and stack[-1] <= L[i]:
        stack.pop()
    # If stack not empty, top is next greater
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] = -1
    # Push current as candidate for elements to the left
    stack.append(L[i])

print(ans)

    
    
