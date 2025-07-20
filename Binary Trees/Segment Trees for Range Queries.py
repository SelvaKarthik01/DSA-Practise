class Node:
    def __init__(self,startinterval,endinterval):
        self.data = 0
        self.startinterval = startinterval
        self.endinterval = endinterval 
        self.left = None 
        self.right = None 
        
def constructTree(L,start,end):
    if start == end:
        #leaf node 
        leaf = Node(start,end)
        leaf.data = L[start]
        return leaf 
    node = Node(start,end)
    mid = (start + end) // 2
    node.left = constructTree(L,start,mid)
    node.right = constructTree(L,mid+1,end)
    node.data = node.left.data + node.right.data
    return node

def display(root):
    if root:
        print(root.data,end = " ")
        display(root.left)
        display(root.right)
        
def query(node,qsi,qei):
    if node.startinterval >= qsi and node.endinterval <= qei:
        # All the Items need to be Taken -> Full Overlapping 
        return node.data 
    elif node.startinterval > qei or node.endinterval < qsi:
        # Completely Outside 
        return 0
    else :
        return query(node.left,qsi,qei) + query(node.right,qsi,qei)

def update(node,index,value):
    if index >= node.startinterval and index <= node.endinterval:
        if index == node.startinterval and index == node.endinterval:
            node.data = value 
            return node.data 
        else:
            leftans = update(node.left,index,value)
            rightans = update(node.right,index,value)
            node.data = leftans + rightans 
            return node.data
    return node.data
        
          
L = [3,8,6,7,-2,-8,4,9]
root = None 
root = constructTree(L,0,len(L)-1)
display(root)
print()
value = int(input("Enter the Value to be Updated : "))
index = int(input("Enter the Index to be Updated : "))
print(query(root,2,6))
update(root,index,value)
display(root)
