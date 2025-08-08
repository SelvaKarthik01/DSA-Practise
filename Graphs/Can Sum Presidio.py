L = eval(input("Enter the List : "))
target = int(input("Enter the Target Variable : "))
from collections import deque
for i in L:
    Queue = deque()
    Queue.append(i)
    found = False
    while(len(Queue) != 0):
        node = Queue.popleft()
        for j in L:
            new_node = node + j
            if new_node == target:
                found = True
            elif new_node < target:
                Queue.append(new_node)
        if found == True:
            break
    if found == True:
        print("Possible ")
        break
else:
    print("Not Possible")