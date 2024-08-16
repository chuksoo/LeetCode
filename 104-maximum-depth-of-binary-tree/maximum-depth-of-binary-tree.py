# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """  
        Uderstand:
            - what should be the output when there's no node
            - what should we return if no left and right node
        Plan:
        -   Using BFS
            * if node is None, return 0
            * if left and right node is None, return 1
            * if left node is None, return 1 plus recursive call to right node
            * if right node is None, return 1 plus recursive call to left node
            * return 1 plus maximum of recursive call to left and right node
        Implement:
        """
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        if root.left is None:
            return 1 + self.maxDepth(root.right)
        
        elif root.right is None:
            return 1 + self.maxDepth(root.left)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        