class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return f"{self.val}"

def populate():
    # Get root value
    try:
        value = input("Enter the value of the root (or 'q' to quit): ")
        if value.lower() == 'q':
            return None
        value = int(value)
    except ValueError:
        print("Invalid input. Please enter an integer or 'q'.")
        return populate()  # Retry on invalid input
    
    # Create root node
    newnode = Node(value)
    
    # Populate left child
    try:
        left = input(f"Enter the value for the left child of {newnode} (or 'q' for none): ")
        if left.lower() != 'q':
            newnode.left = Node(int(left))
            newnode.left = populate()  # Recursively populate left subtree
    except ValueError:
        print("Invalid input. Please enter an integer or 'q'.")
        newnode.left = populate()  # Retry on invalid input
    
    # Populate right child
    try:
        right = input(f"Enter the value for the right child of {newnode} (or 'q' for none): ")
        if right.lower() != 'q':
            newnode.right = Node(int(right))
            newnode.right = populate()  # Recursively populate right subtree
    except ValueError:
        print("Invalid input. Please enter an integer or 'q'.")
        newnode.right = populate()  # Retry on invalid input
    
    return newnode

def display(root, level=0, prefix="Root: "):
    if root is None:
        print("  " * level + prefix + "None")
        return
    print("  " * level + prefix + str(root))
    display(root.left, level + 1, "L--- ")
    display(root.right, level + 1, "R--- ")
    
def level_order(root,search):
    result = -1
    queue = []
    if root is None:
        return result
    queue.append(root)
    while(queue):
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.val == search:
                if queue:
                    return queue.pop(0)
                else:
                    return -1 
    return -1
        

# Main program
root = populate()  # Build the tree
print("\nTree structure:")
display(root) 
search = int(input("Enter the Value to give the SUccessor node in Level Order : "))
print(level_order(root,search))# Display the tree