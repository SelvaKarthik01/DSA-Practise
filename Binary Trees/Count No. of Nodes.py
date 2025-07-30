class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
        self.height = 0
    def __str__(self):
        return f"{self.val}"
    
    
def height(root):
    if root is None:
        return -1 
    return root.height


def populate(root,value):
    if root is None:
        newnode = Node(value)
        newnode.height = 0
        return newnode 
    if root.val > value :
        root.left = populate(root.left,value)
    elif root.val < value:
        root.right = populate(root.right,value)
    root.height = max(height(root.left),height(root.right))+1
    return root 

def balanced(root):
    if root is None:
        return True 
    return abs(height(root.left) - height(root.right)) <= 1 and balanced(root.left) and balanced(root.right)

def preorder(root):
    if root:
        print(root.val,end = " ")
        preorder(root.left)
        preorder(root.right)
        
def display_heights(root):
    if root:
        print(root.val,"-- > ",root.height)
        display_heights(root.left)
        display_heights(root.right)

def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)
        
        
root = None
while(True):
    n = int(input("Enter the Value : "))
    if n == -1 :
        break 
    root = populate(root,n)
preorder(root)
print()
print(count(root))
    
