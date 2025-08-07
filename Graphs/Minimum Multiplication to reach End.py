start = int(input("Enter the Start Number : "))
end = int(input("Enter the End Number : "))
arrlist = eval(input("Enter the Array List : "))
from collections import deque 
Queue = deque()
Queue.append((0,start))
distance = [float("inf")]*(100000)
ans = -1
found = False
while(len(Queue) != 0):
    steps,node = Queue.popleft()
    for i in arrlist:
        newnode = (node * i) % 100000
        if steps + 1 < distance[newnode]:
            if newnode == end:
                ans = steps +1 
                found = True
            else:
                distance[newnode]=steps+1
                Queue.append((steps+1,newnode))
    if found == True:
        break
print("Result : ",ans)

        