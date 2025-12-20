"""
Docstring for Linked Lists.Reverse a Linked List

Time Complexity : O(n)
Space Complexity : O(1)

Another Solution with just Two Pointers Only Possible in Python

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head 
        prev = None 
        curr = head 
        while(curr.next != None):
            prev,curr.next,curr = curr,prev,curr.next
            
        curr.next = prev 
        return cur
        
Same TC and SC 

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
    prev = None 
    curr = head 
    future = head.next 
    while(curr.next != None):
        curr.next = prev 
        prev = curr 
        curr = future 
        future = future.next 
    curr.next = prev 
    return curr 
    
    
        
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = ReverseLL(head)
display(head)