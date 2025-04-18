# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        if root is None:
            return count 

        if root:
            count = 1
            count += self.countNodes(root.left)
            count += self.countNodes(root.right)
        return count
        