"""
Docstring for Linked Lists.Find the Middle of a Linked List

Always Remember in the Odd Count LL fast Pointer will always be in the last 
in a Even Count LL Fast Pointer will alwasy point towards the First None

Time Complexity : O(n//2)
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

def findMiddle(head):
    slow = head 
    fast = head 
    while(fast and fast.next):
        fast = fast.next.next 
        slow = slow.next 
    return slow  
 
        
L = [1,2,3,4,5,6,7,8,9]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
middle = findMiddle(head)
display(head)
print()
display(middle)
    