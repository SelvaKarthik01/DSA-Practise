class Node:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
    def __str__(self):
        return f"{self.val}"
def CreateNode(head,value):
    newnode = Node(value)
    if head is None:
        return newnode
    else:
        curr = head
        while(curr.next is not None):
            curr = curr.next 
        curr.next = newnode
        newnode.prev = curr 
    return head   
def display(head):
    print("Forward Next : ")
    curr = head
    while(curr.next is not None):
        print(curr,end = " -> ")
        curr =curr.next 
    print(curr,"-> NULL")
    print()
    print("Backward Prev : ")
    while(curr.prev is not None):
        print(curr,end = " <- ")
        curr =curr.prev 
    print(curr,"<- NULL")  

def insertNode(head,node_input,pos):
    newnode = Node(node_input)
    if pos == 1:
        head.prev = newnode
        newnode.next = head 
        return newnode 
    if pos > len(L):
        head = CreateNode(head,node_input)
        return head
        
    else:
        k = 1
        curr = head
        while(k < pos and curr is not None):
            k += 1
            curr = curr.next 
        newnode.next,newnode.prev,curr.prev.next,curr.prev = curr,curr.prev,newnode,newnode
        return head 
           
    
L = eval(input("Enter the List to be Added in a Double Linked List : "))
head = None
for i in range(len(L)):
    head = CreateNode(head,L[i])
node_input = input("Enter the Node to be Inserted : ")
pos = int(input("Enter the Position to be Inserted : "))
insertNode(head,node_input,pos)

display(head)