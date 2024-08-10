# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder_dfs = []
        if root is None:
            return preorder_dfs
        
        if root:
            preorder_dfs.append(root.val)
            preorder_dfs = preorder_dfs + self.preorderTraversal(root.left)
            preorder_dfs = preorder_dfs + self.preorderTraversal(root.right)
        return preorder_dfs
        