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

def delete_middle(root):
    if root.next is None:
        return None
        
    fast = root
    slow = root 
    fast = fast.next.next
    while(fast is not None and fast.next is not None):
        slow = slow.next 
        fast = fast.next.next 
    slow.next = slow.next.next
    return root 
    
    

L = eval(input("Enter the List of Nodes : "))
root = None
for i in range(len(L)):
    root = insert(root,L[i])
display(root)
root = delete_middle(root)
display(root)
    
    