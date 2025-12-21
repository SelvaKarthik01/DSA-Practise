"""
Docstring for Linked Lists.Reverse Nodes in a k Group

Time Complexity : O(k) for finding the kth Node + O(k) for reversing the Group K + O(n) for full traversal 
                  Total : O(n)
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
        
def findKthNode(head,k):
    count = 1 
    curr = head 
    while(curr != None and count != k): # If last group has less than K elements keep as it is 
        curr = curr.next 
        count += 1
    return curr

def Reverse(head):
    prev = None
    curr = head  
    while(curr):
        future = curr.next 
        curr.next = prev 
        prev = curr 
        curr = future 
    return prev 

def ReverseKGroups(head,k):
    dummy_head = Node(-1)
    dummy_head.next  = head
    previous = dummy_head
    while(head is not None):
        temp = head 
        kthnode = findKthNode(head,k)
        if kthnode is None:
            previous.next = head
            break
        next_node = kthnode.next
        kthnode.next = None 
        new_head = Reverse(head)
        previous.next = new_head
        previous = temp 
        temp.next = next_node 
        head = next_node
    return dummy_head.next
        
    
L = [1,2,3,4,5,6,7,8,9,10]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
k = int(input("Enter the Value for k : "))
head = ReverseKGroups(head,k)
display(head)