class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
    def __str__(self):
        return f"{self.val}"

def populate(L):
    nodes = {}
    for i in range(len(L)):
        if L[i] not in nodes:
            newnode = Node(L[i])
            nodes[L[i]] = newnode 
        else:
            newnode = nodes[L[i]]
        if 2*i+1 < len(L):
            newnode.left = Node(L[2*i+1])
            nodes[L[2*i+1]]= newnode.left
        if 2*i+2 < len(L):
            newnode.right = Node(L[2*i+2])
            nodes[L[2*i+2]]= newnode.right
    return nodes[L[0]]

def preorder(root):
    if root:
        print(root,end =  " ")
        preorder(root.left)
        preorder(root.right)

L = eval(input("Enter the List of Nodes : "))
root = populate(L)
preorder(root)
        
