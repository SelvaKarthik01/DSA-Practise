"""
Docstring for Linked Lists.Check if a LL is a Palindrome or Not

Time Complexity : 
Space Complexity :

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
    slow=head 
    fast = head 
    while(fast.next is not None and fast.next.next is not None):
        fast = fast.next.next 
        slow = slow.next
    return slow 

def Reverse(head):
    prev = None 
    curr = head 
    while(curr.next != None):
        future = curr.next
        curr.next = prev 
        prev =curr 
        curr = future 
    return prev 

def Palindrome_Check(head):
    slow = findMiddle(head)
    
    second = Reverse(slow.next)
    second_head = second
    first = head 
    while(second != None):
        if first.val != second.val:
            Reverse(second_head)
            return False 
        first = first.next 
        second = second.next
    slow.next = Reverse(slow)
    return True 
        
L = [1,2,3,2,1]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
print(Palindrome_Check(head))
display(head)
    