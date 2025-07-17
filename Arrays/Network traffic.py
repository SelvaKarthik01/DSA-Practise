L = eval(input("Enter the Netwrok traffic"))
window_sizes = eval(input("Enter the List of window Sizes : "))
ans = []
for k in window_sizes:
    i = 0 
    j = k
    max_traffic=[]
    while(j < len(L)):
        max_traffic.append(max(L[i:j]))
        i += 1
        j += 1
    ans.append(min(max_traffic))
    max_traffic = []
print(ans)