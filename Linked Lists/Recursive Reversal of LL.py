"""
Docstring for Linked Lists.Recursive Reversal of LL
"""
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next 
    def __str__(self):
        return f"{self.val}"

def Insert(head,val):
    newnode = Node(val)
    if head == None:
        return newnode 
    else:
        curr = head
        while(curr.next != None):  # Until we reach the Last Node in Linked List  
            curr = curr.next 
        curr.next = newnode 
    return head  

def display(head):
    print(head.val,end="") 
    curr= head.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 

def ReverseLL(head):
    if head is None or head.next is None:
        return head 
    newhead = ReverseLL(head.next)
    front = head.next 
    front.next = head 
    head.next = None 
    return newhead 
        
        
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = ReverseLL(head)
display(head)
    