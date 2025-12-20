"""
Docstring for Linked Lists.Remove the Nth Node from the End

Time Complexity : O(n) Slow and Fast Pointers 
Space Complexity : O(1)

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
        
 
def DeleteNthNode(head,n):
    dummy = Node(-1)
    dummy.next = head 
    fast = dummy   
    for i in range(n):
        fast = fast.next 
    slow = dummy 
    while(fast.next != None):  # At this time fast and slow gap between them is going to be n 
        slow = slow.next 
        fast = fast.next 
    slow.next = slow.next.next
    return dummy.next   
            
L = [1,2,3,4,5]
n = int(input("Enter the Value for N : "))
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = DeleteNthNode(head,n)
display(head)