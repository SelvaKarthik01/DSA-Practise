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
def insertAtPos(root,node_input,pos):
    newnode = Node(node_input)
    if pos == 1:
        newnode.next = root
        return newnode
    else:
        curr = root
        k = 2
        while(k != pos  and curr is not None):
            curr = curr.next
            k += 1
        if curr is not None:
            newnode.next = curr.next 
            curr.next = newnode
        return root
        
    
    
L = eval(input("Enter the List of Nodes : "))
root = None
for i in range(len(L)):
    root = insert(root,L[i])
display(root)
node_input = int(input("Enter the Node Value to be Inserted : "))
pos = int(input("Enter the Position of the Input : "))
root = insertAtPos(root,node_input,pos)
display(root)
