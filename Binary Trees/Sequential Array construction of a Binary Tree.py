class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right 
    def __str__(self):
        return f"{self.val}"


def populate(L):
    nodes = {}
    for parent,child in L:
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)
        if nodes[parent].left is None:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
    return nodes[L[0][0]]

def preorder(root):
    if root:
        print(root,end = " ")
        preorder(root.left)
        preorder(root.right)
            
    

L = eval(input("Enter the Nested Array of Items to Construct the Binary Tree : "))
root = populate(L)
preorder(root)


    