# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        if head is None:
            return values

        current = head   
        while current is not None:
            values.append(current.val)
            current = current.next
            
        result = [0] * len(values)
        stack = []
        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                index = stack.pop()
                result[index] = value
            stack.append(i)
        return result
        