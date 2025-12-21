"""
Docstring for Linked Lists.Rotate a Linked List K times

Time Complexity : O(n) for finding the Length + O(n) for finding the K th Nodes for rotation 
                  Total -> O(n)
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

def findLength(head):
    curr = head 
    count = 0 
    while(curr):
        count += 1
        curr = curr.next 
    return count 
        
def RotateKTimes(head,k):
    if head is None or head.next is None:
        return head 
    length = findLength(head)
    k = k % length
    if k == 0:
        return head 
    dummy = Node(-1)
    dummy.next = head 
    fast = dummy 
    slow = dummy 
    for i in range(k):
        fast = fast.next 
    while(fast.next != None):
        fast = fast.next 
        slow = slow.next 
    new_head = slow.next 
    slow.next = None 
    fast.next = head 
    dummy.next = new_head 
    return dummy.next
        
    
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
k = int(input("Enter the Value for k : "))
head = RotateKTimes(head,k)
display(head)