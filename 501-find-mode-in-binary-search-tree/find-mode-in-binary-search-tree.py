# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        stack = [root]
        while stack:
            popped_node = stack.pop()
            counter[popped_node.val] += 1

            if popped_node.left:
                stack.append(popped_node.left)
            if popped_node.right:
                stack.append(popped_node.right)

        mode_bst = []
        max_freq = max(counter.values())
        for k, v in counter.items():
            if counter[k] == max_freq:
                mode_bst.append(k)
        
        return mode_bst


        