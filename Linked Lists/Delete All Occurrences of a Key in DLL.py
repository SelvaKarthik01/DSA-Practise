"""
Docstring for Linked Lists.Creation, Insertion and Deletion of SLL,DLL,CLL.Delete All Occurrences of a Key in DLL

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

def DeleteKey(head,key):
    if head is None:
        return None 
    dummy = Node(-1)
    dummy.next = head
    head.prev= dummy 
    curr = head 
    while(curr):
        if curr.val == key:
            if curr.prev:
                curr.prev.next = curr.next 
            if curr.next:
                curr.next.prev = curr.prev 
        curr = curr.next 
    new_head = dummy.next 
    if new_head:
        dummy.next.prev = None
    return new_head 
        
L = [10,1,10,4,2,3]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
key = int(input("Enter the Key to be Deleted : "))
head = DeleteKey(head,key)
display_forward(head)
print()
display_backward(head)