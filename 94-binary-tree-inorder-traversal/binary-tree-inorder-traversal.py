# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_dfs = []
        if root is None:
            return inorder_dfs
        
        if root:
            inorder_dfs = inorder_dfs + self.inorderTraversal(root.left)
            inorder_dfs.append(root.val)
            inorder_dfs = inorder_dfs + self.inorderTraversal(root.right)
        return inorder_dfs
        
        