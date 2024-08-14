# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """  
        Understand: Are we returning a list containing string?
                    What happens if the node is none, what's our return value
        Plan:
            # if node is none, return None
            # if node is not None, return the value of the node
            # get left root path 
            # get right root path
            # append to list and return new list
        Implement:
        """
        if root is None:
            return []
        
        if not root.left and not root.right:
            return [str(root.val)]
        
        paths = []
        if root.left:
            for path in self.binaryTreePaths(root.left):
                paths.append(f"{root.val}->{path}")
        
        if root.right:
            for path in self.binaryTreePaths(root.right):
                paths.append(f"{root.val}->{path}")            
                             
        return paths
            
        
