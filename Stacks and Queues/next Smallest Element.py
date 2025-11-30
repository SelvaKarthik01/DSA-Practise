L = eval(input("Enter the List : "))
ans = [0]*len(L)
stack = []
for i in range(len(L)):
    while stack and stack[-1] >= L[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] = -1
    stack.append(L[i])
print(ans)