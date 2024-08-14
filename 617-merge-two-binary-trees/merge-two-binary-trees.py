# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if node 1 is None, return Node 2
        if root1 is None:
            return root2
        # if node 2 is None, return Node 1
        if root2 is None:
            return root1
        # add the value in node 1 and node 2 as the new node 1 
        root1.val += root2.val
        # recursively add left of node 1 to the left of node 2 and right of node 1 to right of node 2
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        # return node 1
        return root1
        