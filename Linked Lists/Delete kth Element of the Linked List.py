"""
Docstring for Linked Lists.Delete kth Element of the Linked List

Time Complexity : O(1) -> Delete Head 
                  O(k) -> Delete All other Nodes 
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
def Length(head):
    count = 0 
    curr = head 
    while(curr):
        curr =curr.next
        count += 1
    return count
def Delete(head,k):
    if head == None:
        return None 
    if k > Length(head):
        return head 
    if k == 1:
        return head.next 
    else:
        curr = head 
        prev = head 
        while(k != 1):
            prev = curr
            curr = curr.next 
            k -= 1
        prev.next = curr.next 
    return head 
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
k = int(input("Enter the Vallue for K : "))
head = Delete(head,k)
display(head)