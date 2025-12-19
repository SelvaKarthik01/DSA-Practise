"""
Docstring for Linked Lists.Length of a Linked List

Time Complexity : O(n)
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
    curr = head 
    while(curr.next != None):
        curr = curr.next 
    curr.next = newnode 
    return head 
def Length(head):
    count = 0 
    curr = head
    while(curr):
        count += 1
        curr = curr.next 
    return count 
n = int(input("Enter the No. of Elements to be Added in Linked List : "))
head = None 
for i in range(n):
    val = int(input())
    head = Insert(head,val)
print("Length: ",Length(head))