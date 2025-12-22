"""
Docstring for Linked Lists.Merge K Sorted Lists

def Merge(first,second):
    dummy = Node(-1)
    previous = dummy 
    while(first != None and second!= None):
        if first.val <= second.val:
            previous.next = first 
            previous = first 
            first = first.next 
        else:
            previous.next = second 
            previous = second 
            second = second.next 
    while(first):
        previous.next = first 
        previous = first 
        first = first.next
    while(second):
        previous.next = second 
        previous = second 
        second = second.next 
    return dummy.next
        
def MergeKLL(heads,k):
    if len(heads) == 0:
        return None 
    first_head = None
    for i in range(len(heads)):
        second_head = heads[i]
        first_head = Merge(first_head,second_head)
    return first_head

TC -> O(k)*O(n)
                  Total -> O(kn) -> O(n^2)
SC ->  O(1) 

Time Complexity : O(nlogn)
Space Complexity : O(n)

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
    if head is None:
        print(None)
        return
    print(head.val,end="") 
    curr= head.next
    while(curr):
        print("->",curr.val,end = "")
        curr = curr.next 
        
import heapq
def MergeKLL(heads,k):
    pq = []
    for i in heads:
        if i:
            heapq.heappush(pq,(i.val,id(i),i))
    dummy = Node(-1)
    previous = dummy 
    while(pq):
        val,_,node = heapq.heappop(pq)
        previous.next = node 
        previous = node 
        if node.next:
            heapq.heappush(pq,(node.next.val,id(node.next),node.next))  # Very Important in Heap Cannot Compare with Node so we need to add reference id 
    return dummy.next 
        

    
k = int(input("Enter the Value for K : "))
heads = []
for i in range(k):
    L = eval(input("Enter Your Linked List : "))
    head = None
    for i in range(len(L)):
        head = Insert(head,L[i])
    heads.append(head)
head = MergeKLL(heads,k)
display(head)