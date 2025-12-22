"""
Docstring for Linked Lists.Sort a Linked List Merge Sort

Time Complexity : O(n) for finding the Middle Element + O(n+n) for Merging the Sorted Arrays + logn for Divide and Conquer
                 Total -> O(nlogn)
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
    fast = head 
    slow = head 
    while(fast.next and fast.next.next):
        fast = fast.next.next 
        slow = slow.next 
    return slow 

def Merge(head1,head2):
    dummy = Node(-1)
    previous = dummy 
    temp1 = head1 
    temp2 = head2 
    while(temp1 and temp2):
        if temp1.val <= temp2.val:
            previous.next = temp1 
            previous = temp1 
            temp1 = temp1.next 
        else:
            previous.next = temp2 
            previous = temp2 
            temp2 = temp2.next 
    while(temp1):
        previous.next = temp1 
        previous = temp1 
        temp1 = temp1.next 
    while(temp2):
        previous.next = temp2 
        previous = temp2 
        temp2 = temp2.next
    return dummy.next  
        
    
def Merge_Sort(head):
    if head is None or head.next is None:
        return  head 
    middle = findMiddle(head)
    right_head = middle.next 
    middle.next = None
    head=Merge_Sort(head)
    right_head = Merge_Sort(right_head)
    return Merge(head,right_head)
        
L = [3,4,2,1,5]
head = None
for i in range(len(L)):
    head = Insert(head,L[i])
head = Merge_Sort(head)
display(head)
