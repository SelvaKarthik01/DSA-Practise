class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
    def __str__(self):
        return f"{self.val}"
def populate(root,value):
    if root is None:
        return Node(value) 
    if root.val > value :
        root.left = populate(root.left,value)
    elif root.val < value:
        root.right = populate(root.right,value)
    return root 
def preorder(root):
    if root:
        print(root.val,end = " ")
        preorder(root.left)
        preorder(root.right)
root = None
while(True):
    n = int(input("Enter the Value : "))
    if n == -1 :
        break 
    root = populate(root,n)
preorder(root)
    
