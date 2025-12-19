"""
Docstring for Linked Lists.Check if Node is Present

Time Compleixty : O(n) Worst Case O(1) Best Case 
Space Compleixty : O(1)
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
def CheckIfPresent(head,check):
    curr = head 
    while(curr):
        if curr.val == check:
            return True
        curr = curr.next  
    return False

L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
check = int(input("Enter the Value to be Checked : "))
print(CheckIfPresent(head,check))
