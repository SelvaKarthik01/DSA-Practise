"""
Docstring for Linked Lists.Starting node in a Loop in a LL

Time Complexity : O(n) + O(n) -> O(n)
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

def StartNodeLoop(head):
    fast = head 
    slow = head 
    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next 
        if fast == slow:
            break 
    slow = head
    while(slow != fast):
        slow = slow.next 
        fast = fast.next 
    return slow 
    
        
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
curr = head 
while(curr.next != None):
    if curr.val == 3:
        start_node = curr
    curr = curr.next
newnode = Node(11)
newnode.next = start_node 
curr.next = newnode 
print(StartNodeLoop(head))

#display(head)
    