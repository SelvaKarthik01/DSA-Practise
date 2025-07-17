class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"{self.val}"
def insert(root,val):
    newnode = Node(val)
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
    print("null")

def searchNode(root,search):
    curr = root
    k = 1
    while(curr is not None):
        if curr.val == search:
            return k
        curr = curr.next 
        k += 1
    return -1
    
L = eval(input("Enter the List of Nodes : "))
root = None
for i in range(len(L)):
    root = insert(root,L[i])
display(root)
search = int(input("Enter the Node to be Searched : "))
print("Found at Position: ",searchNode(root,search))