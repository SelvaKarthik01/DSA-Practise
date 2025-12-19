"""
Docstring for Linked Lists.Creating a Link Lists

Time Complexity : Inserting a Node at Last -> O(n) or O(1) -> if we tail pointer 
Space Compleixty : O(1)

In Linked List you just need to return head in the Backend they will run and check it 
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
L = eval(input("Enter the Elements : "))
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
display(head)
    