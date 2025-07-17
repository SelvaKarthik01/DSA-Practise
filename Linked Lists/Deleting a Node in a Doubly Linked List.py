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

def deleteNode(head,pos):
    if pos == 1:
        head.next.prev = None 
        return head.next 
    k = 1
    curr = head
    while(k < pos and curr is not None):
        curr = curr.next
        k += 1 
    if curr.next is None:
        curr.prev.next = None 
        return head 
    else:
        curr.prev.next = curr.next 
        curr.next.prev = curr.prev
        return head 
        
    
L = eval(input("Enter the List to be Added in a Double Linked List : "))
head = None
for i in range(len(L)):
    head = CreateNode(head,L[i])

display(head)
delete = int(input("Enter the Position to be Deleted : "))
head = deleteNode(head,delete)
display(head)