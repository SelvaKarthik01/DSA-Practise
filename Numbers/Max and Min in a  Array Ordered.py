n = int(input("Enter the Number of Elements : "))
L = eval(input("Enter the List : "))
import heapq
maxq = []
minq = []
for i in range(len(L)):
    heapq.heappush(maxq,-L[i])
    heapq.heappush(minq,L[i])
ans = []
count = 0 
while(count != n):
    max = heapq.heappop(maxq)*-1
    min = heapq.heappop(minq)
    count += 2
    ans.append(max)
    ans.append(min)
print(ans)
    