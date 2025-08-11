n = int(input("Enter the Number : "))
from collections import deque
import math
squares = [i*i for i in range(1,int(math.sqrt(n))+1)]
Queue = deque()
Queue.append((0,0))
visited = set()
visited.add(0)
found = False
ans = -1
while(len(Queue) != 0):
    steps,sum = Queue.popleft()
    for i in squares:
        next = sum + i
        if next == n :
            ans = steps+1
            found = True
            break
        elif next < n and next not in visited:
            visited.add(next)
            Queue.append((steps+1,next))
    if found == True:
        break

print("Minimum : ",ans)

    

        
        
