"""
Docstring for Linked Lists.Insert Head in a Doubly Linked List

Time Complexity : O(1)
Space Complexity : O(1)

"""

class Node:
    def __init__(self,val,next=None,prev=None):
        self.val = val 
        self.next = next 
        self.prev = prev
    def __str__(self):
        return f"{self.val}"

def Insert(head,val):
    newnode = Node(val)
    if head == None:
        return newnode 
    curr = head 
    while(curr.next != None):
        curr = curr.next 
    newnode.prev = curr 
    curr.next = newnode
    return  head 

def display_forward(head):
    if head is None:
        print(None)
        return 
    print(head.val,end = "")
    curr = head
    curr = curr.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
def display_backward(head):
    if head is None:
        print("None")
        return 
    curr = head 
    while(curr.next != None):
        curr = curr.next
    print(curr.val,end="")
    curr= curr.prev
    while(curr):
        print("<-",curr.val,end="")
        curr = curr.prev

def InsertatHead(head,val):
    newnode = Node(val)
    newnode.next = head 
    head.prev = newnode 
    return newnode 

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
node = int(input("Enter the Value of the new Node : "))
head = InsertatHead(head,node)
display_forward(head)
print()
display_backward(head)
    
        