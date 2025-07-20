"""  
103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100



"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        result = []
        queue = []
        if root is None:
            return result
        queue.append(root)
        k = 1
        while queue:
            levelsize = len(queue)
            currentlevel = []
            for i in range(levelsize):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                currentlevel.append(node.val)
            if k & 1 == 0:
                currentlevel.reverse()
            result.append(currentlevel)
            k += 1
        return result 
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        