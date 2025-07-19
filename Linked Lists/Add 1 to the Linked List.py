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
def reverse(root):
    prev = None
    present = root
    while(present is not None):
        prev,present.next,present = present,prev,present.next
    return prev
def add_1(root):
    carry = 0 
    curr = root
    sum = 0
    while(curr is not None):
        if curr == root:
            sum = curr.val + 1 + carry
        else:
            sum = curr.val + carry
        units = sum % 10 
        curr.val = units 
        carry = sum // 10 
        curr = curr.next
    root = reverse(root)
    if carry != 0:
        newnode = Node(carry)
        newnode.next = root 
        return newnode
    return root 

L = eval(input("Enter the List of Nodes : "))
root = None
for i in range(len(L)):
    root = insert(root,L[i])
display(root)
root = reverse(root)
display(root)
root = add_1(root)
display(root)

    
    