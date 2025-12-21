"""
Docstring for Linked Lists.Remove Duplicates from a Sorted DLL

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
        
def DeleteDuplicates(head):
    if head is None or head.next is None:
        return head 
    curr = head
    while(curr and curr.next is not None):
        if curr.val == curr.next.val:
            dup = curr.next 
            
            curr.next = dup.next 
            if dup.next:
                dup.next.prev = curr
        else:
            curr =curr.next  
    return head    
            
L = [1,1,1,2,3,3,3]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])

head = DeleteDuplicates(head)

display_forward(head)
print()
display_backward(head)