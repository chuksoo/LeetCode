# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        
        queue = deque([root])
        
        level = 0
        level_res = 0
        max_level_sum = float('-inf')
        
        while queue:
            level += 1
            sum_at_current_level = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_at_current_level += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
                
            if sum_at_current_level > max_level_sum:
                max_level_sum, level_res = sum_at_current_level, level
        return level_res
                    
                
        