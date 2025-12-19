"""
Docstring for Linked Lists.Delete Node in a Doubly Linked List

Time Complexity : O(n)
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
    print(head.val,end = "")
    curr = head
    curr = curr.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next
         
def display_backward(head):
    curr = head 
    while(curr.next != None):
        curr = curr.next
    print(curr.val,end="")
    curr= curr.prev
    while(curr):
        print("<-",curr.val,end="")
        curr = curr.prev

def DeleteNode(head,node):
    if head.val == node:
        head.next.prev = None 
        head = head.next
        return head 
    curr = head
    while(curr.val != node):
        curr = curr.next 
    curr.prev.next = curr.next 
    if curr.next != None:
        curr.next.prev = curr.prev 
    return head 

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
node = int(input("Enter tthe Node to be Deleted : "))
head = DeleteNode(head,node)
display_forward(head)
print()
display_backward(head)

    
        