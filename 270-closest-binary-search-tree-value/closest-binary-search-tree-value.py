# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def get_best_val(node, best):
            if not node:
                return best

            if (abs(node.val - target) < abs(best - target)) or (abs(node.val - target) == abs(best - target) and node.val < best):
                best = node.val

            if target < node.val:
                return get_best_val(node.left, best)
            else:
                return get_best_val(node.right, best)

        return get_best_val(root, root.val)        


        