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

def rotateRight(p):
    c = p.left 
    t = c.right 
    p.left = t 
    c.right = p 
    p.height = max(height(p.left), height(p.right)) + 1
    c.height = max(height(c.left), height(c.right)) + 1
    return c 
def rotateLeft(c):
    p = c.right
    t = p.left 
    c.right = t 
    p.left = c 
    p.height = max(height(p.left), height(p.right)) + 1
    c.height = max(height(c.left), height(c.right)) + 1
    return p
    
def balanced(root):
    if root is None:
        return True 
    return abs(height(root.left) - height(root.right)) <= 1 and balanced(root.left) and balanced(root.right)

def getBalance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)

def rotate(root):
    balance = getBalance(root)
    
    # Left heavy
    if balance > 1:
        if getBalance(root.left) >= 0:
            # Left-Left Case
            return rotateRight(root)
        else:
            # Left-Right Case
            root.left = rotateLeft(root.left)
            return rotateRight(root)

    # Right heavy
    if balance < -1:
        if getBalance(root.right) <= 0:
            # Right-Right Case
            return rotateLeft(root)
        else:
            # Right-Left Case
            root.right = rotateRight(root.right)
            return rotateLeft(root)
    
    return root 
        

def insert(root,value):
    if root is None :
        root = Node(value)
        return root 
    elif value < root.val:
        root.left = insert(root.left,value)
    elif value > root.val:
        root.right = insert(root.right,value)
    root.height = max(height(root.left),height(root.right)) + 1 
    return rotate(root)

def inorder(root):
    if root :
        inorder(root.left) 
        print(root.val,end = " ")
        inorder(root.right)
        
def printTree(root, level=0, prefix="Root: "):
    if root is not None:
        print("    " * level + prefix + str(root.val))
        printTree(root.left, level + 1, prefix="L--- ")
        printTree(root.right, level + 1, prefix="R--- ")
        

root = None
while(True):
    n = int(input("Enter the Number to be Inserted : "))
    if n != -1:
        root = insert(root,n)
    else :
        break 
inorder(root)
print(balanced(root))
printTree(root)

 
    