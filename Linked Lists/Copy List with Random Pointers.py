"""
Docstring for Linked Lists.Copy List with Random Pointers

Time Complexity : O(n) for Creating New Nodes + O(n) ofr joining the random points + O(n) for finally combining the Cloned Nodes 
Space Complexity : O(1) Auxiliary Space : O(n) for cloning N nodes 

"""
class Node:
    def __init__(self,val,next=None,random = None):
        self.val = val
        self.next = next 
        self.random = random
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
        
def DeepCopy(head):
    curr = head 
    while(curr):
        newnode = Node(curr.val)
        newnode.next = curr.next 
        curr.next = newnode 
        curr = newnode.next
    curr = head 
    while(curr and curr.next):
        newnode = curr.next 
        if curr.random:
            newnode.random = curr.random.next
        curr = newnode.next 
    dummy = Node(-1)
    previous = dummy 
    curr = head 
    while(curr and curr.next):
        previous.next = curr.next
        if curr.next: 
            curr.next = curr.next.next 
        previous = previous.next  
        curr =curr.next 
    return dummy.next 
    
def display_with_random(head):
    curr = head
    while curr:
        rand = curr.random.val if curr.random else None
        print(f"[Val:{curr.val}, Random:{rand}]", end=" -> ")
        curr = curr.next
    print("None")

# Test Case 1
# List: 1 -> 2 -> 3
# Random: 1->3, 2->1, 3->2

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.random = head.next.next        # 1 -> 3
head.next.random = head             # 2 -> 1
head.next.next.random = head.next   # 3 -> 2

print("Original List:")
display_with_random(head)

copy_head = DeepCopy(head)

print("\nCopied List:")
display_with_random(copy_head)
