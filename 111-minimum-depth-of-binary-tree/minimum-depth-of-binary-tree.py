# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Using Breadth First Search
        # if node is None, return 0
        if root is None:
            return 0
        
        # if no left and right node, return 1
        if root.left is None and root.right is None:
            return 1
        
        # if no left node, return 1 plus recursive call to right node
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        # if no right node, return 1 plus recursive call to left node
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        
        # return 1 plus min(recursive call to left node, recursive call to right node)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        