# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        level_order = [] # to hold list of level

        if root is None:
            return level_order

        queue = deque([root])
        while queue:
            level_size = len(queue) # number of nodes at this level
            current_level = [] # collect values at this level

            for _ in range(level_size):
                popped_node = queue.popleft()
                current_level.append(popped_node.val)

                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)
            level_order.append(current_level)
        return level_order
  
                
        