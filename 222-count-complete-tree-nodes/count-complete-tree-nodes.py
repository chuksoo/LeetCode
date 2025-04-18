# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # # First way to solve this
        # # base case
        # count = 0
        # if root is None:
        #     return count 

        # # recursive case
        # if root:
        #     count = 1
        #     count += self.countNodes(root.left)
        #     count += self.countNodes(root.right)
        # return count

        # second way
        # base case
        if root is None:
            return 0

        # recursive case
        if root.left is None and root.right is None:
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) # add 1 for root node
        