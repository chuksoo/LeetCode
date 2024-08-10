# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder_dfs = []
        # if root is null, return empty list
        if root is None:
            return postorder_dfs
        # traverse the tree by starting from the left subtree, right subtree and root
        # checking if root is not None, append the value of that root to list
        if root:
            postorder_dfs = postorder_dfs + self.postorderTraversal(root.left)
            postorder_dfs = postorder_dfs + self.postorderTraversal(root.right)
            postorder_dfs.append(root.val)
        return postorder_dfs 