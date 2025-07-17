class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val}"
def insert(root,val):
    newnode = Node(val,None)
    if root == None:
        return newnode
    curr = root
    while(curr.next is not None):
        curr = curr.next 
    curr.next = newnode
    return root
def display(root):
    curr = root
    while(curr is not None):
        print(curr,end=" -> ")
        curr = curr.next
    print("END")

def deleteAtPos(root,pos):
    if pos == 1:
        return root.next 
    k = 1
    curr = root
    while(k != pos-1 and curr is not None):
        curr  = curr.next 
        k += 1
    curr.next = curr.next.next 
    return root
    
    
    
L = eval(input("Enter the List of Nodes : "))
root = None
for i in range(len(L)):
    root = insert(root,L[i])
display(root)
pos = int(input("Enter the Position of the Input : "))
root = deleteAtPos(root,pos)
display(root)
